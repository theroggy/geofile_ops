
import logging
import logging.config
import os
from pathlib import Path
from typing import Any, AnyStr, List, Optional, Tuple, Union

from .util import geofileops_ogr
from .util import geofileops_gpd

################################################################################
# Some init
################################################################################

logger = logging.getLogger(__name__)

################################################################################
# The real work
################################################################################

def select(
        input_path: str,
        output_path: str,
        sqlite_stmt: str,
        input_layer: str = None,        
        output_layer: str = None,
        verbose: bool = False,
        force: bool = False):
    """
    Execute an sqlite style SQL query on the file. 

    The result is written to the output file specified.

    Args:
        input_path (str): the input file
        output_path (str): the file to write the result to
        sqlite_stmt (str): the statement to execute
        input_layer (str, optional): input layer name. Optional if the input file only contains one layer.
        output_layer (str, optional): input layer name. Optional if the input file only contains one layer.
        verbose (bool, optional): write more info to the output. Defaults to False.
        force (bool, optional): overwrite existing output file(s). Defaults to False.
    """

    return geofileops_ogr.select(
            input_path=input_path,
            output_path=output_path,
            sqlite_stmt=sqlite_stmt,
            input_layer=input_layer,        
            output_layer=output_layer,
            verbose=verbose,
            force=force)

def convexhull(
        input_path: str,
        output_path: str,
        input_layer: str = None,
        output_layer: str = None,
        nb_parallel: int = -1,
        verbose: bool = False,
        force: bool = False):
    """
    Applies a convexhull operation on the input file.
    
    The result is written to the output file specified. 

    Args:
        input_path (str): the input file
        output_path (str): the file to write the result to
        input_layer (str, optional): input layer name. Optional if the input 
                file only contains one layer.
        output_layer (str, optional): input layer name. Optional if the input 
                file only contains one layer.
        nb_parallel (int, optional): the number of parallel processes to use. 
                If not specified, all available processors will be used.
        verbose (bool, optional): write more info to the output. 
                Defaults to False.
        force (bool, optional): overwrite existing output file(s). 
                Defaults to False.
    """

    return geofileops_ogr.convexhull(
            input_path=input_path,
            output_path=output_path,
            input_layer=input_layer,
            output_layer=output_layer,
            nb_parallel=nb_parallel,
            verbose=verbose,
            force=force)

def buffer(
        input_path: str,
        output_path: str,
        buffer: float,
        quadrantsegments: int = 5,
        input_layer: str = None,
        output_layer: str = None,
        nb_parallel: int = -1,
        verbose: bool = False,
        force: bool = False):
    """
    Applies a buffer operation on geometry column of the input file.
    
    The result is written to the output file specified. 

    Args:
        input_path (str): the input file
        output_path (str): the file to write the result to
        buffer (float): the buffer size to apply
        quadrantsegments (int): the number of points an arc needs to be 
                approximated with. Defaults to 5.
        input_layer (str, optional): input layer name. Optional if the input 
                file only contains one layer.
        output_layer (str, optional): input layer name. Optional if the input 
                file only contains one layer.
        nb_parallel (int, optional): the number of parallel processes to use. 
                If not specified, all available processors will be used.
        verbose (bool, optional): write more info to the output. 
                Defaults to False.
        force (bool, optional): overwrite existing output file(s). 
                Defaults to False.
    """

    return geofileops_gpd.buffer(
            input_path=input_path,
            output_path=output_path,
            buffer=buffer,
            quadrantsegments=quadrantsegments,
            input_layer=input_layer,
            output_layer=output_layer,
            nb_parallel=nb_parallel,
            verbose=verbose,
            force=force)

def simplify(
        input_path: str,
        output_path: str,
        tolerance: float,        
        input_layer: str = None,        
        output_layer: str = None,
        nb_parallel: int = -1,
        verbose: bool = False,
        force: bool = False):
    """
    Applies a simplify operation on geometry column of the input file.
    
    The result is written to the output file specified. 

    Args:
        input_path (str): the input file
        output_path (str): the file to write the result to
        tolerance (float): the tolerancy to use when simplifying
        input_layer (str, optional): input layer name. Optional if the input 
                file only contains one layer.
        output_layer (str, optional): input layer name. Optional if the input 
                file only contains one layer.
        nb_parallel (int, optional): the number of parallel processes to use. 
                If not specified, all available processors will be used.
        verbose (bool, optional): write more info to the output. 
                Defaults to False.
        force (bool, optional): overwrite existing output file(s). 
                Defaults to False.
    """

    return geofileops_ogr.simplify(
            input_path=input_path,
            output_path=output_path,
            tolerance=tolerance,
            input_layer=input_layer,
            output_layer=output_layer,
            nb_parallel=nb_parallel,
            verbose=verbose,
            force=force)

def intersect(
        input1_path: str,
        input2_path: str,
        output_path: str,
        input1_layer: str = None,
        input2_layer: str = None,
        output_layer: str = None,
        nb_parallel: int = -1,
        verbose: bool = False,
        force: bool = False):
    """
    Calculate the pairwise intersection of alle features in input1 with all 
    features in input2.
    
    Args:
        input1_path (str): the 1st input file
        input2_path (str): the 2nd input file
        output_path (str): the file to write the result to
        input1_layer (str, optional): input layer name. Optional if the  
                file only contains one layer.
        input2_layer (str, optional): input layer name. Optional if the  
                file only contains one layer.
        output_layer (str, optional): output layer name. Optional if the  
                file only contains one layer.
        nb_parallel (int, optional): the number of parallel processes to use. 
                If not specified, all available processors will be used.
        verbose (bool, optional): write more info to the output. 
                Defaults to False.
        force (bool, optional): overwrite existing output file(s). 
                Defaults to False.
    """

    return geofileops_ogr.intersect(
            input1_path=input1_path,
            input2_path=input2_path,
            output_path=output_path,
            input1_layer=input1_layer,
            input2_layer=input2_layer,
            output_layer=output_layer,
            nb_parallel=nb_parallel,
            verbose=verbose,
            force=force)

def export_by_location(
        input_to_select_from_path: str,
        input_to_compare_with_path: str,
        output_path: str,
        input1_layer: str = None,
        input2_layer: str = None,
        output_layer: str = None,
        nb_parallel: int = -1,
        verbose: bool = False,
        force: bool = False):
    """
    Exports all features in input_to_select_from_path that intersect with any 
    features in input_to_compare_with_path.
    
    Args:
        input_to_select_from_path (str): the 1st input file
        input_to_compare_with_path (str): the 2nd input file
        output_path (str): the file to write the result to
        input1_layer (str, optional): input layer name. Optional if the  
                file only contains one layer.
        input2_layer (str, optional): input layer name. Optional if the  
                file only contains one layer.
        output_layer (str, optional): output layer name. Optional if the  
                file only contains one layer.
        nb_parallel (int, optional): the number of parallel processes to use. 
                If not specified, all available processors will be used.
        verbose (bool, optional): write more info to the output. 
                Defaults to False.
        force (bool, optional): overwrite existing output file(s). 
                Defaults to False.
    """

    return geofileops_ogr.export_by_location(
            input_to_select_from_path=input_to_select_from_path,
            input_to_compare_with_path=input_to_compare_with_path,
            output_path=output_path,
            input1_layer=input1_layer,
            input2_layer=input2_layer,
            output_layer=output_layer,
            nb_parallel=nb_parallel,
            verbose=verbose,
            force=force)

def export_by_distance(
        input_to_select_from_path: str,
        input_to_compare_with_path: str,
        output_path: str,
        max_distance: float,
        input1_layer: str = None,
        input2_layer: str = None,
        output_layer: str = None,
        nb_parallel: int = -1,
        verbose: bool = False,
        force: bool = False):
    """
    Exports all features in input_to_select_from_path that are within the 
    distance specified of any features in input_to_compare_with_path.
    
    Args:
        input_to_select_from_path (str): the 1st input file
        input_to_compare_with_path (str): the 2nd input file
        output_path (str): the file to write the result to
        max_distance (float): maximum distance
        input1_layer (str, optional): input layer name. Optional if the  
                file only contains one layer.
        input2_layer (str, optional): input layer name. Optional if the  
                file only contains one layer.
        output_layer (str, optional): output layer name. Optional if the  
                file only contains one layer.
        nb_parallel (int, optional): the number of parallel processes to use. 
                If not specified, all available processors will be used.
        verbose (bool, optional): write more info to the output. 
                Defaults to False.
        force (bool, optional): overwrite existing output file(s). 
                Defaults to False.
    """

    return geofileops_ogr.export_by_distance(
            input_to_select_from_path=input_to_select_from_path,
            input_to_compare_with_path=input_to_compare_with_path,
            output_path=output_path,
            max_distance=max_distance,
            input1_layer=input1_layer,
            input2_layer=input2_layer,
            output_layer=output_layer,
            nb_parallel=nb_parallel,
            verbose=verbose,
            force=force)

def dissolve(
        input_path: Union[str, 'os.PathLike[Any]'],  
        output_path: Union[str, 'os.PathLike[Any]'],
        groupby_columns: Optional[List[str]] = None,
        aggfunc: str = None,
        explodecollections: bool = False,
        keep_cardsheets: bool = False,
        input_layer: str = None,        
        output_layer: str = None,
        input_cardsheets_path: Union[str, 'os.PathLike[Any]'] = None,
        nb_parallel: int = -1,
        verbose: bool = False,
        force: bool = False):
    """
    Applies a dissolve operation on geometry column of the input file.
    
    The result is written to the output file specified. 

    Args:
        input_path (str): the input file
        output_path (str): the file to write the result to
        groupby_columns: (List[str]): list of columns to group on before applying the union.
        explodecollections (bool): True to convert all multi-geometries to 
                singular ones after the dissolve. Defaults to False.
        input_layer (str, optional): input layer name. Optional if the  
                file only contains one layer.
        output_layer (str, optional): input layer name. Optional if the  
                file only contains one layer.
        nb_parallel (int, optional): the number of parallel processes to use. 
                If not specified, all available processors will be used.
        verbose (bool, optional): write more info to the output. 
                Defaults to False.
        force (bool, optional): overwrite existing output file(s). 
                Defaults to False.
    """
    
    return geofileops_gpd.dissolve(
            input_path=input_path,
            output_path=output_path,
            groupby_columns=groupby_columns,
            aggfunc=aggfunc,
            explodecollections=explodecollections,
            keep_cardsheets=keep_cardsheets,
            input_layer=input_layer,        
            output_layer=output_layer,
            input_cardsheets_path=input_cardsheets_path,
            nb_parallel=nb_parallel,
            verbose=verbose,
            force=force)
    
if __name__ == '__main__':
    raise Exception("Not implemented!")