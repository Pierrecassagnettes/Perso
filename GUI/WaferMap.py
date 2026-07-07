# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 09:26:54 2023

@author: kevin.froberger

Goal : Plot a wafer map using information from a file

"""

######################################
###
#   Packages
###
######################################
from matplotlib.patches import Circle, Ellipse
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib as mpl
import sys
from pathlib import Path
mpl.rcParams['axes.formatter.useoffset'] = False  # remove the default offest formating in matplotlib plots


class WaferMap:
    def __init__(self, die_x, die_y, wafer_size, data_dict, notch='south', offset_x=0, offset_y=0):
        """
        Parameters
        ----------
        die_x : integer of float
            Number giving the size of the die in the x direction that will be showed
            in the plot. The number depends on the orientation of the wafer if the dies
            are not a square
        die_y : integer of float
            Number giving the size of the die in the y direction that will be showed
            in the plot. The number depends on the orientation of the wafer if the dies
            are not a square
        wafer_size : integer of float
            Number giving the size of the tested wafer in um
        data_dict : dictionary
            Dictionary containing all the data. The key has to be the die written as
            followed : 'die_i' where i is the number of the die. The case is ignored for more flexibility.
        notch : String
            A string giving the position of the notch. Default : 'north'

        Other parameters available:
            z_range : list of the elements, the first one is the smallest
                Sets the limit of the colormap
            colorbar_title : string
                Gives the colorbar a title
            title : string
                Gives the wafermap a title
        They can be changed by calling the object.
        Example : wafer.title = 'bonjour'

        Returns
        -------
        None.

        """
        self.wafer_size = wafer_size
        self.die_x = die_x
        self.die_y = die_y
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.loaded_map = None
        self.data_dict = data_dict
        self.notch = notch
        self.rows = 0
        self.columns = 0
        self.fig_size = None
        self.Z = []
        self.X = []
        self.Y = []
        self.z_range = 'auto'
        self.colorbar_title = None
        self.title = None
        self.annotation_fontsize = 7
        self.annotation_precision = 3
        self.annotation_format = 'g'
        self.is_wave =False
    def load_map(self, path):
        """
        Parameters
        ----------
        path : path
            Path on the computer to the wafermap setup
        """
        if not os.path.exists(path):
            raise Exception(f"File not found : {path}")
            
        # FIX: Added ndmin=2 to force a 2D matrix layout even if the file has 1 row
        self.loaded_map = np.genfromtxt(path, delimiter="\t", ndmin=2)
        
        self.rows = len(self.loaded_map)
        self.columns = len(self.loaded_map[0])
        self.X = np.linspace(0, self.columns - 1, self.columns) * self.die_x
        self.Y = np.linspace(self.rows - 1, 0, self.rows) * self.die_y
        self.Z = np.zeros((self.rows, self.columns))
        nb_dies = 0
        
        # Robust fix: safely convert keys to string before calling .lower()
        data_dict_lower_keys = [str(key).lower() for key in self.data_dict]
        
        for i in range(self.rows):
            for j in range(self.columns):
                nb_dies += 1
                # Secure safe check for nan values inside the loaded text map matrix
                if np.isnan(self.loaded_map[i, j]) or self.loaded_map[i, j] == 0:
                    self.Z[i, j] = np.nan
                elif 'die_' + str(int(self.loaded_map[i, j])) not in data_dict_lower_keys:
                    self.Z[i, j] = np.nan
                else:
                    for key in self.data_dict.keys():
                        if str(int(self.loaded_map[i, j])).lower() == str(key).lower().replace("die_", ""):
                            # numpy automatically converts scientific strings like "1.76e18" into floats here
                            self.Z[i, j] = self.data_dict[key]
                            
        return nb_dies
    def plot_map(self, ax=None, fig=None, title=None):
        """
        Plotting the wafermap with dynamic scaling for extreme values (TLM metrics)

        Returns
        -------
        fig, ax
        """
        self.title = title
        axis_width_inches = ax.get_position().width * fig.get_size_inches()[0]
        total_dies_span = self.columns + 3
        die_width_points = (axis_width_inches * 72) / total_dies_span
        
        fmt = getattr(self, 'annotation_format', 'g')
        divisor = 2.8 if fmt == 'f' else 3.8
        max_font = 11.5 if fmt == 'f' else 9
        
        dynamic_fontsize = max(4, min(max_font, die_width_points / divisor))
            
        if ax is None:
            if self.fig_size != None:
                fig, ax = plt.subplots(figsize=self.fig_size)
            else:
                fig, ax = plt.subplots()
        self.loaded_map[self.loaded_map == 0] = np.nan

        Z_scaled = self.Z.copy()
        multiplier_str = ""
        
        # Filter out nans and zeros to evaluate the true numeric range
        valid_ticks = self.Z[~np.isnan(self.Z) & (self.Z != 0)]
        if valid_ticks.size > 0 and self.is_wave == False:
            max_val = np.max(np.abs(valid_ticks))
            # Apply auto-scaling if values are engineering extremes
            if max_val >= 1000 or max_val < 0.1 and self.is_wave == False:
                exponent = int(np.floor(np.log10(max_val)))
                # Shift exponent by 2 to get clean values like 135 instead of 1.35
                plot_exponent = exponent - 2
                scale_factor = 10**plot_exponent
                Z_scaled = self.Z / scale_factor
                multiplier_str = f" *1e{plot_exponent}"

        # Colormap mesh plotting using the scaled dataset
        if self.z_range != 'auto':
            vmin_val = self.z_range[0]
            vmax_val = self.z_range[1]
            if multiplier_str:
                vmin_val /= scale_factor
                vmax_val /= scale_factor
            c = ax.pcolormesh(
                self.X,
                self.Y,
                Z_scaled,
                vmin=vmin_val,
                vmax=vmax_val,
                cmap="cividis",
                shading="nearest",
                edgecolors="k",
                linewidth=0.5,
            )
        else:
            c = ax.pcolormesh(
                self.X,
                self.Y,
                Z_scaled,
                cmap="cividis",
                shading="nearest",
                edgecolors="k",
                linewidth=0.5,
            )

        # --- ANNOTATIONS (PLOTS CLEAN SCALED VALUES INSIDE DIES) ---
        prec = self.annotation_precision if isinstance(self.annotation_precision, int) else 3
        for i in range(len(self.X)):
            for j in range(len(self.Y)):
                if not np.isnan(Z_scaled[j][i]):
                    bbox = dict(boxstyle="square", facecolor='white', edgecolor='black', alpha=0.8)
                    val = Z_scaled[j][i]
                    
                    # Formats to max 3 significant figures without scientific sub-strings
                    val_str = f"{val:.{prec}{fmt}}"
                    ax.text(self.X[i], self.Y[j], val_str,
                            ha='center', va='center', color='black',
                            fontsize=dynamic_fontsize, bbox=bbox)

        # Drawing the wafer
        wafer = Circle(
            (
                (self.columns / 2 - 1 / 2) * self.die_x + self.offset_x,
                (self.rows / 2 - 1 / 2) * self.die_y - self.offset_y,
            ),
            self.wafer_size / 2,
            fill=None,
            linewidth=2,
        )
        ax.add_patch(wafer)

        # Notch
        if self.notch.lower() == 'north':
            notch = Ellipse(
                ((self.columns / 2 - 1 / 2) * self.die_x + self.offset_x,
                 (self.rows / 2 - 1 / 2) * self.die_y + self.wafer_size / 2 - self.offset_y),
                width=self.wafer_size / 10,
                height=self.wafer_size / 20,
                fill=True,
                linewidth=2,
                color='black')
        elif self.notch.lower() == "south":
            notch = Ellipse(
                ((self.columns / 2 - 1 / 2) * self.die_x + self.offset_x,
                 (self.rows / 2 - 1 / 2) * self.die_y - self.wafer_size / 2 - self.offset_y),
                width=self.wafer_size / 10,
                height=self.wafer_size / 20,
                fill=True,
                linewidth=2,
                color='black')
        elif self.notch.lower() == "east":
            notch = Ellipse(
                ((self.columns / 2 - 1 / 2) * self.die_x + self.wafer_size / 2 + self.offset_x,
                 (self.rows / 2 - 1 / 2) * self.die_y - self.offset_y),
                height=self.wafer_size / 10,
                width=self.wafer_size / 20,
                fill=True,
                linewidth=2,
                color='black')
        elif self.notch.lower() == "west":
            notch = Ellipse(
                ((self.columns / 2 - 1 / 2) * self.die_x - self.wafer_size / 2 + self.offset_x,
                 (self.rows / 2 - 1 / 2) * self.die_y - self.offset_y),
                height=self.wafer_size / 10,
                width=self.wafer_size / 20,
                fill=True,
                linewidth=2,
                color='black')
        else:
            raise Exception("Wrong definition of the notch parameter.")
        ax.add_patch(notch)

        # Axis, for now they are turned off
        ax.set_xticks(np.linspace(0, self.columns - 1, self.columns) * self.die_x)
        ax.set_xticklabels([str(int(i)) for i in np.linspace(0, self.columns - 1, self.columns)])
        ax.set_yticks(np.linspace(0, self.rows - 1, self.rows) * self.die_y)
        ax.set_yticklabels([str(int(i)) for i in np.linspace(0, self.rows - 1, self.rows)])
        ax.set_xlim([-2 * self.die_x, (self.columns + 1) * self.die_x])
        ax.set_ylim([-2 * self.die_y, (self.rows + 1) * self.die_y])
        ax.axis("equal")
        ax.axis('off')

        # Title
        if self.title is not None:
            ax.set_title(f'{self.title}')
        # Colorbar
        clb = fig.colorbar(c, ax=ax, fraction=0.046, pad=0.04)
        if self.is_wave == True:
            clb.formatter.set_scientific(False)
            clb.formatter.set_useOffset(False)
            clb.update_ticks()
        cb_title = f"{self.colorbar_title if self.colorbar_title is not None else ''}{multiplier_str}".strip()
        if cb_title:
            clb.ax.set_title(cb_title)
            
        fig.tight_layout()
        return fig, ax

    def plot_map_die_number(self):
        """
        Plots a wafermap with the number of the dies as the value for each die.
        A 0 in the map will result on a white square with no number on it.

        Returns
        -------
        None.

        """

        # Plotting the map
        fig, ax = plt.subplots()
        self.loaded_map[self.loaded_map == 0] = np.nan
        c = ax.pcolormesh(
            self.X,
            self.Y,
            self.loaded_map,
            cmap="cividis",
            shading="nearest",
            edgecolors="k",
            linewidth=0.5,
        )

        # Annotations
        for i in range(len(self.X)):
            for j in range(len(self.Y)):
                if not np.isnan(self.loaded_map[j][i]):
                    ax.text(self.X[i], self.Y[j],
                            f'{self.loaded_map[j][i]:.0f}', ha='center', va='center')

        # Drawing the wafer
        wafer = Circle(
            (
                (self.rows / 2 - 1 / 2) * self.die_x,
                (self.columns / 2 - 1 / 2) * self.die_y,
            ),
            self.wafer_size / 2,
            fill=None,
            linewidth=2,
        )
        ax.add_patch(wafer)

        # Axis, for now they are turned off
        ax.set_xticks(np.linspace(0, self.columns - 1, self.columns) * self.die_x)
        ax.set_xticklabels(
            [str(int(i)) for i in np.linspace(0, self.columns - 1, self.columns)]
        )
        ax.set_yticks(np.linspace(0, self.rows - 1, self.rows) * self.die_y)
        ax.set_yticklabels(
            [str(int(i)) for i in np.linspace(0, self.rows - 1, self.rows)]
        )
        ax.set_xlim([-2 * self.die_x, (self.columns + 1) * self.die_x])
        ax.set_ylim([-2 * self.die_y, (self.rows + 1) * self.die_y])
        ax.axis("equal")
        ax.axis('off')

        # Colorbar
        fig.colorbar(c, ax=ax)


def main(is_wave,data_dict, fig, ax, title="Wafermap", wafer_name=None, colorbar='auto', is_loss=False ):
    # Close all previous MPL figures

    # Create a dictionnary
    # data_dict = {'die_1': 15,
    #             'die_2': 12,
    #             'die_3': 10,
    #             'die_4': 8,
    #             'die_5': 5,
    #             'die_10': 1,
    #             'die_11': np.nan,
    #             'die_52': 20}

    # The wafermap itself
    
    die_x = 21050
    die_y = 21450  # in um
    wafer_size = 200000  # in um
    # Path to the folder inside of which the wafer map infos are (.txt file)
    base_path = r"W:\50-DEVELOPMENT\TEST\Temporary data database\Data"
    map_position = os.path.join(base_path, wafer_name, 'Map infos')
    map_position = os.path.join(map_position ,"Die_vs_XY.txt")
    # Going to the correct place, where the map info are
    if not os.path.isfile(map_position):
        map_position = os.path.join(base_path,'D24S2097_23', 'Map infos',"Die_vs_XY.txt")
    loaded_map = np.genfromtxt(map_position, delimiter="\t")
    rows = len(loaded_map)
    columns = len(loaded_map[0])
    if rows*columns == 16 :
        wafer_size = 100000
    # Creating the object
    wafer_map = WaferMap(die_x, die_y, wafer_size, data_dict)
    wafer_map.z_range = colorbar
    
    # Si c'est un loss, on force 1 seul chiffre après la virgule (format 'f')
    if is_loss:
        wafer_map.annotation_precision = 1
        wafer_map.annotation_format = 'f'
    if is_wave:
        wafer_map.annotation_precision = 5
        wafer_map.is_wave = True
    # Load the wafermap parameters from the text file, it should be the second function to do
    wafer_map.load_map(map_position)
    
    # Choosing to put the notch at the bottom
    wafer_map.notch = 'south'
    # Plotting the wafermap with the data
    wafer_map.plot_map(ax=ax,fig=fig,title=title)
    # Plotting the wafermap with the die numbers
    #wafer_map.plot_map_die_number()
    return 


if __name__ == "__main__":
    main()
