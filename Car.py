{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "purple-fighter",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "statutory-syndrome",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('car data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "terminal-vitamin",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Car_Name</th>\n",
       "      <th>Year</th>\n",
       "      <th>Selling_Price</th>\n",
       "      <th>Present_Price</th>\n",
       "      <th>Kms_Driven</th>\n",
       "      <th>Fuel_Type</th>\n",
       "      <th>Seller_Type</th>\n",
       "      <th>Transmission</th>\n",
       "      <th>Owner</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>ritz</td>\n",
       "      <td>2014</td>\n",
       "      <td>3.35</td>\n",
       "      <td>5.59</td>\n",
       "      <td>27000</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>sx4</td>\n",
       "      <td>2013</td>\n",
       "      <td>4.75</td>\n",
       "      <td>9.54</td>\n",
       "      <td>43000</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ciaz</td>\n",
       "      <td>2017</td>\n",
       "      <td>7.25</td>\n",
       "      <td>9.85</td>\n",
       "      <td>6900</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>wagon r</td>\n",
       "      <td>2011</td>\n",
       "      <td>2.85</td>\n",
       "      <td>4.15</td>\n",
       "      <td>5200</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>swift</td>\n",
       "      <td>2014</td>\n",
       "      <td>4.60</td>\n",
       "      <td>6.87</td>\n",
       "      <td>42450</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Car_Name  Year  Selling_Price  Present_Price  Kms_Driven Fuel_Type  \\\n",
       "0     ritz  2014           3.35           5.59       27000    Petrol   \n",
       "1      sx4  2013           4.75           9.54       43000    Diesel   \n",
       "2     ciaz  2017           7.25           9.85        6900    Petrol   \n",
       "3  wagon r  2011           2.85           4.15        5200    Petrol   \n",
       "4    swift  2014           4.60           6.87       42450    Diesel   \n",
       "\n",
       "  Seller_Type Transmission  Owner  \n",
       "0      Dealer       Manual      0  \n",
       "1      Dealer       Manual      0  \n",
       "2      Dealer       Manual      0  \n",
       "3      Dealer       Manual      0  \n",
       "4      Dealer       Manual      0  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "twelve-likelihood",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Dealer' 'Individual']\n",
      "['Petrol' 'Diesel' 'CNG']\n",
      "['Manual' 'Automatic']\n",
      "[0 1 3]\n"
     ]
    }
   ],
   "source": [
    "print(df['Seller_Type'].unique())\n",
    "print(df['Fuel_Type'].unique())\n",
    "print(df['Transmission'].unique())\n",
    "print(df['Owner'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ethical-richmond",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Car_Name         0\n",
       "Year             0\n",
       "Selling_Price    0\n",
       "Present_Price    0\n",
       "Kms_Driven       0\n",
       "Fuel_Type        0\n",
       "Seller_Type      0\n",
       "Transmission     0\n",
       "Owner            0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "##check missing values\n",
    "df.isnull().sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "searching-february",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(301, 9)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "genetic-turner",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "surrounded-outline",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Car_Name', 'Year', 'Selling_Price', 'Present_Price', 'Kms_Driven',\n",
       "       'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "sudden-falls",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_dataset=df[['Year','Selling_Price','Present_Price','Kms_Driven','Fuel_Type','Seller_Type','Transmission','Owner']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "blond-latter",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Year</th>\n",
       "      <th>Selling_Price</th>\n",
       "      <th>Present_Price</th>\n",
       "      <th>Kms_Driven</th>\n",
       "      <th>Fuel_Type</th>\n",
       "      <th>Seller_Type</th>\n",
       "      <th>Transmission</th>\n",
       "      <th>Owner</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2014</td>\n",
       "      <td>3.35</td>\n",
       "      <td>5.59</td>\n",
       "      <td>27000</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2013</td>\n",
       "      <td>4.75</td>\n",
       "      <td>9.54</td>\n",
       "      <td>43000</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017</td>\n",
       "      <td>7.25</td>\n",
       "      <td>9.85</td>\n",
       "      <td>6900</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2011</td>\n",
       "      <td>2.85</td>\n",
       "      <td>4.15</td>\n",
       "      <td>5200</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2014</td>\n",
       "      <td>4.60</td>\n",
       "      <td>6.87</td>\n",
       "      <td>42450</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Year  Selling_Price  Present_Price  Kms_Driven Fuel_Type Seller_Type  \\\n",
       "0  2014           3.35           5.59       27000    Petrol      Dealer   \n",
       "1  2013           4.75           9.54       43000    Diesel      Dealer   \n",
       "2  2017           7.25           9.85        6900    Petrol      Dealer   \n",
       "3  2011           2.85           4.15        5200    Petrol      Dealer   \n",
       "4  2014           4.60           6.87       42450    Diesel      Dealer   \n",
       "\n",
       "  Transmission  Owner  \n",
       "0       Manual      0  \n",
       "1       Manual      0  \n",
       "2       Manual      0  \n",
       "3       Manual      0  \n",
       "4       Manual      0  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "balanced-poster",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_dataset['Current Year']=2020"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "tutorial-album",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Year</th>\n",
       "      <th>Selling_Price</th>\n",
       "      <th>Present_Price</th>\n",
       "      <th>Kms_Driven</th>\n",
       "      <th>Fuel_Type</th>\n",
       "      <th>Seller_Type</th>\n",
       "      <th>Transmission</th>\n",
       "      <th>Owner</th>\n",
       "      <th>Current Year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2014</td>\n",
       "      <td>3.35</td>\n",
       "      <td>5.59</td>\n",
       "      <td>27000</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2013</td>\n",
       "      <td>4.75</td>\n",
       "      <td>9.54</td>\n",
       "      <td>43000</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017</td>\n",
       "      <td>7.25</td>\n",
       "      <td>9.85</td>\n",
       "      <td>6900</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2011</td>\n",
       "      <td>2.85</td>\n",
       "      <td>4.15</td>\n",
       "      <td>5200</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2014</td>\n",
       "      <td>4.60</td>\n",
       "      <td>6.87</td>\n",
       "      <td>42450</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Year  Selling_Price  Present_Price  Kms_Driven Fuel_Type Seller_Type  \\\n",
       "0  2014           3.35           5.59       27000    Petrol      Dealer   \n",
       "1  2013           4.75           9.54       43000    Diesel      Dealer   \n",
       "2  2017           7.25           9.85        6900    Petrol      Dealer   \n",
       "3  2011           2.85           4.15        5200    Petrol      Dealer   \n",
       "4  2014           4.60           6.87       42450    Diesel      Dealer   \n",
       "\n",
       "  Transmission  Owner  Current Year  \n",
       "0       Manual      0          2020  \n",
       "1       Manual      0          2020  \n",
       "2       Manual      0          2020  \n",
       "3       Manual      0          2020  \n",
       "4       Manual      0          2020  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "dramatic-chester",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_dataset['no_year']=final_dataset['Current Year']- final_dataset['Year']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "charitable-paragraph",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Year</th>\n",
       "      <th>Selling_Price</th>\n",
       "      <th>Present_Price</th>\n",
       "      <th>Kms_Driven</th>\n",
       "      <th>Fuel_Type</th>\n",
       "      <th>Seller_Type</th>\n",
       "      <th>Transmission</th>\n",
       "      <th>Owner</th>\n",
       "      <th>Current Year</th>\n",
       "      <th>no_year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2014</td>\n",
       "      <td>3.35</td>\n",
       "      <td>5.59</td>\n",
       "      <td>27000</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2013</td>\n",
       "      <td>4.75</td>\n",
       "      <td>9.54</td>\n",
       "      <td>43000</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017</td>\n",
       "      <td>7.25</td>\n",
       "      <td>9.85</td>\n",
       "      <td>6900</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2011</td>\n",
       "      <td>2.85</td>\n",
       "      <td>4.15</td>\n",
       "      <td>5200</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2014</td>\n",
       "      <td>4.60</td>\n",
       "      <td>6.87</td>\n",
       "      <td>42450</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Year  Selling_Price  Present_Price  Kms_Driven Fuel_Type Seller_Type  \\\n",
       "0  2014           3.35           5.59       27000    Petrol      Dealer   \n",
       "1  2013           4.75           9.54       43000    Diesel      Dealer   \n",
       "2  2017           7.25           9.85        6900    Petrol      Dealer   \n",
       "3  2011           2.85           4.15        5200    Petrol      Dealer   \n",
       "4  2014           4.60           6.87       42450    Diesel      Dealer   \n",
       "\n",
       "  Transmission  Owner  Current Year  no_year  \n",
       "0       Manual      0          2020        6  \n",
       "1       Manual      0          2020        7  \n",
       "2       Manual      0          2020        3  \n",
       "3       Manual      0          2020        9  \n",
       "4       Manual      0          2020        6  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "awful-watch",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_dataset.drop(['Year'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "parliamentary-participation",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Selling_Price</th>\n",
       "      <th>Present_Price</th>\n",
       "      <th>Kms_Driven</th>\n",
       "      <th>Fuel_Type</th>\n",
       "      <th>Seller_Type</th>\n",
       "      <th>Transmission</th>\n",
       "      <th>Owner</th>\n",
       "      <th>Current Year</th>\n",
       "      <th>no_year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3.35</td>\n",
       "      <td>5.59</td>\n",
       "      <td>27000</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.75</td>\n",
       "      <td>9.54</td>\n",
       "      <td>43000</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>7.25</td>\n",
       "      <td>9.85</td>\n",
       "      <td>6900</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2.85</td>\n",
       "      <td>4.15</td>\n",
       "      <td>5200</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4.60</td>\n",
       "      <td>6.87</td>\n",
       "      <td>42450</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>Dealer</td>\n",
       "      <td>Manual</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Selling_Price  Present_Price  Kms_Driven Fuel_Type Seller_Type  \\\n",
       "0           3.35           5.59       27000    Petrol      Dealer   \n",
       "1           4.75           9.54       43000    Diesel      Dealer   \n",
       "2           7.25           9.85        6900    Petrol      Dealer   \n",
       "3           2.85           4.15        5200    Petrol      Dealer   \n",
       "4           4.60           6.87       42450    Diesel      Dealer   \n",
       "\n",
       "  Transmission  Owner  Current Year  no_year  \n",
       "0       Manual      0          2020        6  \n",
       "1       Manual      0          2020        7  \n",
       "2       Manual      0          2020        3  \n",
       "3       Manual      0          2020        9  \n",
       "4       Manual      0          2020        6  "
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "after-humor",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_dataset=pd.get_dummies(final_dataset,drop_first=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "hundred-attempt",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Selling_Price</th>\n",
       "      <th>Present_Price</th>\n",
       "      <th>Kms_Driven</th>\n",
       "      <th>Owner</th>\n",
       "      <th>Current Year</th>\n",
       "      <th>no_year</th>\n",
       "      <th>Fuel_Type_Diesel</th>\n",
       "      <th>Fuel_Type_Petrol</th>\n",
       "      <th>Seller_Type_Individual</th>\n",
       "      <th>Transmission_Manual</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3.35</td>\n",
       "      <td>5.59</td>\n",
       "      <td>27000</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.75</td>\n",
       "      <td>9.54</td>\n",
       "      <td>43000</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>7.25</td>\n",
       "      <td>9.85</td>\n",
       "      <td>6900</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2.85</td>\n",
       "      <td>4.15</td>\n",
       "      <td>5200</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4.60</td>\n",
       "      <td>6.87</td>\n",
       "      <td>42450</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Selling_Price  Present_Price  Kms_Driven  Owner  Current Year  no_year  \\\n",
       "0           3.35           5.59       27000      0          2020        6   \n",
       "1           4.75           9.54       43000      0          2020        7   \n",
       "2           7.25           9.85        6900      0          2020        3   \n",
       "3           2.85           4.15        5200      0          2020        9   \n",
       "4           4.60           6.87       42450      0          2020        6   \n",
       "\n",
       "   Fuel_Type_Diesel  Fuel_Type_Petrol  Seller_Type_Individual  \\\n",
       "0                 0                 1                       0   \n",
       "1                 1                 0                       0   \n",
       "2                 0                 1                       0   \n",
       "3                 0                 1                       0   \n",
       "4                 1                 0                       0   \n",
       "\n",
       "   Transmission_Manual  \n",
       "0                    1  \n",
       "1                    1  \n",
       "2                    1  \n",
       "3                    1  \n",
       "4                    1  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "biblical-wright",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Selling_Price</th>\n",
       "      <th>Present_Price</th>\n",
       "      <th>Kms_Driven</th>\n",
       "      <th>Owner</th>\n",
       "      <th>Current Year</th>\n",
       "      <th>no_year</th>\n",
       "      <th>Fuel_Type_Diesel</th>\n",
       "      <th>Fuel_Type_Petrol</th>\n",
       "      <th>Seller_Type_Individual</th>\n",
       "      <th>Transmission_Manual</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Selling_Price</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.878983</td>\n",
       "      <td>0.029187</td>\n",
       "      <td>-0.088344</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.236141</td>\n",
       "      <td>0.552339</td>\n",
       "      <td>-0.540571</td>\n",
       "      <td>-0.550724</td>\n",
       "      <td>-0.367128</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Present_Price</th>\n",
       "      <td>0.878983</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.203647</td>\n",
       "      <td>0.008057</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.047584</td>\n",
       "      <td>0.473306</td>\n",
       "      <td>-0.465244</td>\n",
       "      <td>-0.512030</td>\n",
       "      <td>-0.348715</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kms_Driven</th>\n",
       "      <td>0.029187</td>\n",
       "      <td>0.203647</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.089216</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.524342</td>\n",
       "      <td>0.172515</td>\n",
       "      <td>-0.172874</td>\n",
       "      <td>-0.101419</td>\n",
       "      <td>-0.162510</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Owner</th>\n",
       "      <td>-0.088344</td>\n",
       "      <td>0.008057</td>\n",
       "      <td>0.089216</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.182104</td>\n",
       "      <td>-0.053469</td>\n",
       "      <td>0.055687</td>\n",
       "      <td>0.124269</td>\n",
       "      <td>-0.050316</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Current Year</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>no_year</th>\n",
       "      <td>-0.236141</td>\n",
       "      <td>0.047584</td>\n",
       "      <td>0.524342</td>\n",
       "      <td>0.182104</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.064315</td>\n",
       "      <td>0.059959</td>\n",
       "      <td>0.039896</td>\n",
       "      <td>-0.000394</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fuel_Type_Diesel</th>\n",
       "      <td>0.552339</td>\n",
       "      <td>0.473306</td>\n",
       "      <td>0.172515</td>\n",
       "      <td>-0.053469</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.064315</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.979648</td>\n",
       "      <td>-0.350467</td>\n",
       "      <td>-0.098643</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fuel_Type_Petrol</th>\n",
       "      <td>-0.540571</td>\n",
       "      <td>-0.465244</td>\n",
       "      <td>-0.172874</td>\n",
       "      <td>0.055687</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.059959</td>\n",
       "      <td>-0.979648</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.358321</td>\n",
       "      <td>0.091013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Seller_Type_Individual</th>\n",
       "      <td>-0.550724</td>\n",
       "      <td>-0.512030</td>\n",
       "      <td>-0.101419</td>\n",
       "      <td>0.124269</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.039896</td>\n",
       "      <td>-0.350467</td>\n",
       "      <td>0.358321</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.063240</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Transmission_Manual</th>\n",
       "      <td>-0.367128</td>\n",
       "      <td>-0.348715</td>\n",
       "      <td>-0.162510</td>\n",
       "      <td>-0.050316</td>\n",
       "      <td>NaN</td>\n",
       "      <td>-0.000394</td>\n",
       "      <td>-0.098643</td>\n",
       "      <td>0.091013</td>\n",
       "      <td>0.063240</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                        Selling_Price  Present_Price  Kms_Driven     Owner  \\\n",
       "Selling_Price                1.000000       0.878983    0.029187 -0.088344   \n",
       "Present_Price                0.878983       1.000000    0.203647  0.008057   \n",
       "Kms_Driven                   0.029187       0.203647    1.000000  0.089216   \n",
       "Owner                       -0.088344       0.008057    0.089216  1.000000   \n",
       "Current Year                      NaN            NaN         NaN       NaN   \n",
       "no_year                     -0.236141       0.047584    0.524342  0.182104   \n",
       "Fuel_Type_Diesel             0.552339       0.473306    0.172515 -0.053469   \n",
       "Fuel_Type_Petrol            -0.540571      -0.465244   -0.172874  0.055687   \n",
       "Seller_Type_Individual      -0.550724      -0.512030   -0.101419  0.124269   \n",
       "Transmission_Manual         -0.367128      -0.348715   -0.162510 -0.050316   \n",
       "\n",
       "                        Current Year   no_year  Fuel_Type_Diesel  \\\n",
       "Selling_Price                    NaN -0.236141          0.552339   \n",
       "Present_Price                    NaN  0.047584          0.473306   \n",
       "Kms_Driven                       NaN  0.524342          0.172515   \n",
       "Owner                            NaN  0.182104         -0.053469   \n",
       "Current Year                     NaN       NaN               NaN   \n",
       "no_year                          NaN  1.000000         -0.064315   \n",
       "Fuel_Type_Diesel                 NaN -0.064315          1.000000   \n",
       "Fuel_Type_Petrol                 NaN  0.059959         -0.979648   \n",
       "Seller_Type_Individual           NaN  0.039896         -0.350467   \n",
       "Transmission_Manual              NaN -0.000394         -0.098643   \n",
       "\n",
       "                        Fuel_Type_Petrol  Seller_Type_Individual  \\\n",
       "Selling_Price                  -0.540571               -0.550724   \n",
       "Present_Price                  -0.465244               -0.512030   \n",
       "Kms_Driven                     -0.172874               -0.101419   \n",
       "Owner                           0.055687                0.124269   \n",
       "Current Year                         NaN                     NaN   \n",
       "no_year                         0.059959                0.039896   \n",
       "Fuel_Type_Diesel               -0.979648               -0.350467   \n",
       "Fuel_Type_Petrol                1.000000                0.358321   \n",
       "Seller_Type_Individual          0.358321                1.000000   \n",
       "Transmission_Manual             0.091013                0.063240   \n",
       "\n",
       "                        Transmission_Manual  \n",
       "Selling_Price                     -0.367128  \n",
       "Present_Price                     -0.348715  \n",
       "Kms_Driven                        -0.162510  \n",
       "Owner                             -0.050316  \n",
       "Current Year                            NaN  \n",
       "no_year                           -0.000394  \n",
       "Fuel_Type_Diesel                  -0.098643  \n",
       "Fuel_Type_Petrol                   0.091013  \n",
       "Seller_Type_Individual             0.063240  \n",
       "Transmission_Manual                1.000000  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_dataset.corr()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "aging-gathering",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "searching-entrepreneur",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x246d1e21a48>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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PRRRWjGvEhGlBstTotzH+5iI98F48FoRUT5jGUe5IpN5lfcFZZNMdNCdJKVcikD4yq8LIU6O/GNwtlxa55DGO4cQYp0QYqsQYmt3d7fqb12DrvCNGuLyKjg85EpbWom0xMunAPMqZYdE+ZQoW/C7n3IBy9SJ432cWcyr2Yn3gRq/+ykXsDyldEhHGce8SumQ6rzK737KFWnvoJNSHgr+exjAnxFYQ64rGLoSwX8PB3c/BGB6xMvrg9viba/X2I445xibvrullMuklMsqKytVf6u2m2E2qi+R2ahDVZE58RsnSqF4+RRgXqXskCifEmULfvdTLmCZOnG8jzOLeTU78T5Q43c/5QKWp5QO6SjjmFcpHVKdV/ndT7kirR10QgibEKIo9H8ApwLYBuBJAJcEd7sEwBPB/z8J4GIRcAKAgWCYyr8COFUIUSqEKA0e56/Bvw0KIU4QQggAF485ltY5kjaj3Ibbzl8cvmFD8WhnlNvGeyiitGJeJSJKDZanRLmP9zER74Px4LUionzGMo5yRSbzKu8LyiaGNB+/GsCfA31nMAB4SEr5rBDiHwAeFUJcDqAdwPnB/Z8BcDqANgBOAJcCgJSyTwhxI4B/BPe7QUrZF/z/1wD8FoAFwF+CPwDwkxjnSJpOJ7C6pQZz16/A4SEXqorMmFFu42KRlHWYV4mIUoPlKVHu431MxPtgPHitiCifsYyjXJHJvMr7grJJWjvopJR7ASzS2N4LYJXGdgng6zGOdR+A+zS2bwXQmuw5xkunE2iqLERTZeHRHooorZhXiYhSg+UpUe7jfUzE+2A8eK2IKJ+xjKNckcm8yvuCskXa16AjIiIiIiIiIiIiIiIiolHsoCMiIiIiIiIiIiIiIiLKIHbQEREREREREREREREREWUQO+iIiIiIiIiIiIiIiIiIMogddEREREREREREREREREQZxA46IiIiIiIiIiIiIiIiogxiBx0RERERERERERERERFRBrGDjoiIiIiIiIiIiIiIiCiD2EFHRERERERERERERERElEHsoCMiIiIiIiIiIiIiIiLKIHbQEREREREREREREREREWUQO+iIiIiIiIiIiIiIiIiIMogddEREREREREREREREREQZxA46IiIiIiIiIiIiIiIiogxiBx0RERERERERERERERFRBrGDjoiIiIiIiIiIiIiIiCiD2EFHRERERERERERERERElEHsoCMiIiIiIiIiIiIiIiLKIHbQEREREREREREREREREWUQO+iIiIiIiIiIiIiIiIiIMogddEREREREREREREREREQZlJEOOiGEXgjxjhDi6eDvM4UQbwgh2oQQjwghTMHtBcHf24J/nxFxjO8Ft38khPh8xPbVwW1tQojvRmzXPAcRERERERERERERERHRZMrUDLoNAHZE/H4zgNullLMB9AO4PLj9cgD9we23B/eDEGI+gAsBtABYDeDnwU4/PYC7AJwGYD6ALwb3jXcOIiIiIiIiIiIiIiIiokmT9g46IUQ9gH8G8Ovg7wLASgB/DO5yP4C1wf+fFfwdwb+vCu5/FoCHpZRuKeU+AG0Algd/2qSUe6WUHgAPAzgrwTmIiIiIiIiIiIiIiIiIJk0mZtD9N4DvAFCCv5cDOCKl9AV/PwigLvj/OgAfA0Dw7wPB/cPbx7wm1vZ451ARQqwTQmwVQmzt7u6e4FskSi/mU8oFzKeUK5hXKRcwn1KuYF6lXMB8SrmA+ZRyBfMq5QLmU8oVae2gE0KsAXBYSvlWOs9zNKSUd0spl0kpl1VWVk52cog0MZ9SLmA+pVzBvEq5gPmUcgXzKuUC5lPKBcynlCuYVykXMJ9SrjCk+fj/BOBMIcTpAMwA7ADuAFAihDAEZ7jVAzgU3P8QgOkADgohDACKAfRGbA+JfI3W9t445yAiIiIiIiIiIiIiIiKaNGmdQSel/J6Usl5KOQPAhQC2SCn/BcALAM4N7nYJgCeC/38y+DuCf98ipZTB7RcKIQqEEDMBNAN4E8A/ADQLIWYKIUzBczwZfE2scxARERERERERERERERFNmkysQaflagBXCSHaEFgv7t7g9nsBlAe3XwXguwAgpdwO4FEAHwJ4FsDXpZT+4Oy4KwH8FcAOAI8G9413DiIiIiIiIiIiIiIiIqJJk+4Ql2FSyhcBvBj8/14AyzX2cQE4L8brfwjghxrbnwHwjMZ2zXMQERERERERERERERERTabJmkFHRERERERERERERERENCWxg46IiIiIiIiIiIiIiIgog9hBR0RERERERERERERERJRB7KAjIiIiIiIiIiIiIiIiyiB20BERERERERERERERERFlEDvoiIiIiIiIiIiIiIiIiDKIHXREREREREREREREREREGcQOOiIiIiIiIiIiIiIiIqIMYgcdERERERERERERERERUQaxg46IiIiIiIiIiIiIiIgog9hBR0RERERERERERERERJRB7KAjIiIiIiIiIiIiIiIiyiBDsjsKISoBfAXAjMjXSSkvS32yiIiIiIiIiIiIiIiIiPJT0h10AJ4A8DKAvwHwpyc5RERERERERERERERERPltPB10Vinl1WlLCREREREREREREREREdEUMJ416J4WQpyetpQQERERERERERERERERTQHj6aDbgEAnnUsIMSiEGBJCDKYrYURERERERERERERERET5KOkQl1LKonQmhIiIiIiIiIiIiIiIiGgqSHoGnQj4VyHEtcHfpwshlqcvaURERERERERERERERET5ZzwhLn8O4EQAXwr+PgzgrpSniIiIiIiIiIiIiIiIiCiPjaeD7ngp5dcBuABAStkPwBTvBUIIsxDiTSHEe0KI7UKI64PbZwoh3hBCtAkhHhFCmILbC4K/twX/PiPiWN8Lbv9ICPH5iO2rg9vahBDfjdiueQ4iIiIiIiIiIiIiIiKiyTSeDjqvEEIPQAKAEKISgJLgNW4AK6WUiwAsBrBaCHECgJsB3C6lnA2gH8Dlwf0vB9Af3H57cD8IIeYDuBBAC4DVAH4uhNAH03MXgNMAzAfwxeC+iHMOIiIiIiIiIiIiIiIiokkzng66TQD+DKBKCPFDAK8A+FG8F8iA4eCvxuCPBLASwB+D2+8HsDb4/7OCvyP491VCCBHc/rCU0i2l3AegDcDy4E+blHKvlNID4GEAZwVfE+scRERERERERERERERERJPGkOyOUsrfCSHeArAKgACwVkq5I9HrgrPc3gIwG4HZbnsAHJFS+oK7HARQF/x/HYCPg+fzCSEGAJQHt78ecdjI13w8ZvvxwdfEOgcRERERERERERERERHRpEl6Bp0QYhOAMinlXVLKO5PpnAMAKaVfSrkYQD0CM97mTiilaSKEWCeE2CqE2Nrd3T3ZySHSxHxKuYD5lHIF8yrlAuZTyhXMq5QLmE8pFzCfUq5gXqVcwHxKuWI8IS7fAnCNEGKPEOJWIcSy8ZxISnkEwAsATgRQIoQIzd6rB3Ao+P9DAKYDQPDvxQB6I7ePeU2s7b1xzjE2XXdLKZdJKZdVVlaO5y0RZQzzKeUC5lPKFcyrlAuYTylXMK9SLmA+pVzAfEq5gnmVcgHzKeWKpDvopJT3SylPB3AcgI8A3CyE2B3vNUKISiFESfD/FgCnANiBQEfducHdLgHwRPD/TwZ/R/DvW6SUMrj9QiFEgRBiJoBmAG8C+AeAZiHETCGECcCFAJ4MvibWOYiIiIiIiIiIiIiIiIgmTdJr0EWYjUCYykYEOtviqQVwf3AdOh2AR6WUTwshPgTwsBDiJgDvALg3uP+9AB4UQrQB6EOgww1Syu1CiEcBfAjAB+DrUko/AAghrgTwVwB6APdJKbcHj3V1jHMQERERERERERERERERTZqkO+iEELcA+AKAPQAeAXBjMGxlTFLK9wEs0di+F4H16MZudwE4L8axfgjghxrbnwHwTLLnICIiIiIiIiIiIiIiIppM45lBtwfAiVLKnnQlhoiIiIiIiIiIiIiIiCjfJeygE0LMlVLuRGC9twYhREPk36WUb6crcURERERERERERERERET5JpkZdFcBWAfgpxp/kwBWpjRFRERERERERERERERERHksYQedlHKdEEIH4Bop5f9lIE1EREREREREREREREREeUuXzE5SSgXAnWlOCxEREREREREREREREVHeS6qDLmizEOIcIYRIW2qIiIiIiIiIiIiIiIiI8tx4Ouj+H4A/APAIIQaFEENCiME0pYuIiIiIiIiIiIiIiIgoLyVcgy5ESlmUzoQQERERERERERERERERTQVJddAJIQwATgMwN7jpQwB/lVL60pUwIiIiIiIiIiIiIiIionyUMMSlEKIOwHYA3wQwDUAdgO8A2C6EmJbe5BERERERERERERERERHll2Rm0P0QwC+klP8duVEIsR7AjwFckoZ0EREREREREREREREREeWlZDroTpBSfnnsRinlJiHER6lPEhEREREREREREREREVH+ShjiEsBInL85U5UQIiIiIiIiIiIiIiIioqkgmRl0xUKIszW2CwD2FKeHiIiIiIiIiIiIiIiIKK8l00H3dwBnxPjbSylMCxEREREREREREREREVHeS9hBJ6W8NJkDCSEukVLef/RJIiIiIiIiIiIiIiIiIspfyaxBl6wNKTwWERERERERERERERERUV5KZQedSOGxiIiIiIiIiIiIiIiIiPJSMmvQJUum8FhZRVEk9vc60DXoQrXdjBnlNuh07I+k7MJ8SkSUGixPiXIf72PKVcy7k4PXnYjyGcs4yhXMq5QLUp1P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PVCeSr1Qrko9UJ5KvVCuSj1Qnko9UJ5KvVCuSj1Qnkq9qEkHnZk1unsf8IZhTH4vMN/M9jCzJuBkYGnW/A8Czid0zq0fccAiIiIiIiIiIiIiIiIiFVKrZ9DdAxwMPGBmS4ErgY7Mh+5+db4J3X1rfF7djUADcKG7rzazc4Bl7r6UcEvLqcCVZgbwN3c/ftTWRkRERERERERERERERKREteqgy2gBNgBHAA5Y/J+3gw7A3W8Absgadlbi9VEVj1RERERERERERERERESkAmrVQbeTmX0JWMW2jrkMr01IIiIiIiIiIiIiIiIiIqOvVh10DYRbUFqOz9RBJyIiIiIiIiIiIiIiImNWrTro1rr7OTVatoiIiIiIiIiIiIiIiEjNTKjRcnNdOSciIiIiIiIiIiIiIiIy5tWqg+7IGi1XREREREREREREREREpKZq0kHn7i/VYrkiIiIiIiIiIiIiIiIitVarK+hERERERERERERERERExiV10ImIiIiIiIiIiIiIiIhUkTroRERERERERERERERERKpIHXQiIiIiIiIiIiIiIiIiVaQOOhEREREREREREREREZEqUgediIiIiIiIiIiIiIiMK3N33Q0zK/tv7q671Tp0GSMaax2AiIiIiIiIiIiIiIhINT3/7DOcdP6dZU93xacOG4VoZDzSFXQiIiIiIiIiIiIiIiIiVaQOOhEREREREREREREREZEqUgediIiIiIiIiIiIiIiISBWpg05ERERERERERERERESkitRBJyIiIiIiIiIiIiIiIlJF6qATERERERERERERERERqSJ10ImIiIiIiIiIiIiIiIhUkTroRERERERERERERERERKqosdYBDJeZHQ38CGgALnD3b2d93gxcChwCbABOcvc15S6np6ePB59/hbXt3ew0rZkpzQ3sucNkWponsmZDB+s2djFregu7bT+Zv728Zcj7DR3dNE2YwKbuXpoaGujp62Nq80TaO3uY3NxId28/W3q2Mrt1EgfMnk5j44SB5a5c2876jd1Mb2lk59YWdp8xlQkTrGC8/f0+ENfkpkZ6+vrYcUoz83acUtK0T73YwdMvdTClqZFZ05vZbYcpAIPWNXteyWXOaW2hrx/Wb9q2HZ5+acvAPGe3NrO1b9vn+eIK272ddRu72GlaM40NRuukppLWoxqS61xoPappU2cXD7d1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\n",
      "text/plain": [
       "<Figure size 1800x1800 with 110 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(final_dataset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "korean-powder",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "complimentary-longitude",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABCoAAARjCAYAAACpAsVuAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/Il7ecAAAACXBIWXMAAAsTAAALEwEAmpwYAAB3zUlEQVR4nOzdd5hddZ0/8Pd3JhWSQEJJAglFDE26iCgKCCrFAop1cW0oq6zurtj7T1yxsOKqK7pgRQUXkN4FVFC6gkiVSA2QAoQQ0jPz/f2REBKIw4zJ3Dnmvl7PM0/mnPO9937OTeCZed/P+ZxSaw0AAABAE3QMdAEAAAAATxJUAAAAAI0hqAAAAAAaQ1ABAAAANIagAgAAAGgMQQUAAADQGIIKAAAA4BlKKT8spUwvpdz8N46XUsq3SimTSyk3lVJ2WR2vK6gAAAAAVubHSfbv4fgBSSYt/To8yXdXx4sKKgAAAIBnqLVenuTRHpYclOTEusTVSdYtpYxf1dcVVAAAAAB/j42T3L/c9pSl+1bJoFV9gt4o79+9tuJ1oD/V47480CXAatF9wf8NdAmwyn7xql8PdAmwWrzuM88d6BJgtRj+xfPKQNfQn9bY32m/d82/ZMklG086vtZ6/ECV86SWBBUAAABAsywNJVYlmHggycTltics3bdKXPoBAAAA/D3OTvL2pXf/2D3JrFrrQ6v6pDoqAAAAgGcopZycZO8k65dSpiT5fJLBSVJr/V6S85McmGRykrlJ3rU6XldQAQAAAD0oHWv0CI6/qdb61mc5XpP86+p+XZd+AAAAAI0hqAAAAAAaQ1ABAAAANIagAgAAAGgMwzQBAACgB+06THOg6KgAAAAAGkNQAQAAADSGoAIAAABoDDMqAAAAoAdmVLSWjgoAAACgMQQVAAAAQGMIKgAAAIDGMKMCAAAAemBGRWvpqAAAAAAaQ1ABAAAANIagAgAAAGgMMyoAAACgB6WYUdFKOioAAACAxhBUAAAAAI0hqAAAAAAaQ1ABAAAANIZhmgAAANCD0mGYZivpqAAAAAAaQ1ABAAAANIagAgAAAGgMMyoAAACgB2ZUtJaOCgAAAKAxBBUAAABAYwgqAAAAgMYwowIAAAB6YEZFa+moAAAAABpDUAEAAAA0hqACAAAAaAwzKgAAAKAHZlS0lo4KAAAAoDEEFQAAAEBjCCoAAACAxhBUAAAAAI1hmCYAAAD0wDDN1tJRAQAAADSGoAIAAABoDEEFAAAA0BhmVAAAAEAPzKhoLR0VAAAAQGMIKgAAAIDGEFQAAAAAjWFGBQAAAPTAjIrW0lEBAAAANIagAgAAAGgMQQUAAADQGGZUAAAAQA9KMaOilXRUAAAAAI0hqAAAAAAaQ1ABAAAANIagAgAAAGgMwzQBAACgB6XDMM1W0lEBAAAANIagAgAAAGgMQQUAAADQGGZUAAAAQA/MqGgtHRUAAABAYwgqAAAAgMYQVAAAAACNYUYFAAAA9MCMitbSUQEAAAA0hqACAAAAaAxBBQAAANAYZlQAAABAD8yoaC0dFQAAAEBjCCoAAACAxhBUAAAAAI0hqAAAAAAawzBNAAAA6IFhmq2lowIAAABoDEEFAAAA0BiCCgAAAKAxzKgAAACAHphR0Vo6KgAAAIDGEFQAAAAAjSGoAAAAABrDjAoAAADogRkVraWjAgAAAGgMQQUAAADQGIIKAAAAoDHMqAAAAIAemFHRWjoqAAAAgMYQVAAAAACNIagAAAAAGkNQAQAAADSGYZoAAADQg1IM02wlHRUAAABAYwgqAAAAgMYQVAAAAACNYUYFAAAA9KB0mFHRSjoqAAAAgMYQVAAAAACNIagAAAAAGsOMCgAAAOiBGRWtpaMCAAAAaAwdFf/gfvDPn86rt98j02fPzPZfPHSgy4EeXX7FLfnSl05Jd3d33viGPXL44fuvcPxHP7okp572u3R2dmbMmBE5+ktvz8Ybr7fs+BNPzMuBr/pCXr7vjvnc597a6vJpY7XWHH3Gnbn8tkczbHBHjn7rNnnexJHPWHfL/bPzyZNvy4JF3dlzmzH51OsmpZSnPoH50a/vy9fO/muu/OIeGT1iSGbPW5yP/ezWPPTY/Czuqnn3yzbJ6184vpWnRpt7/jc/nY0O3CuL587P1e/8RGbecOsz1uz76xMzfPyG6Zo3P0ly2SvfnQUzHs3WH3pntnjPG9O9uCsLZjyaq9/9qcy978FWnwJk8IH/ko4td00WLcjC07+R+tBfn7Fm0Mvfns6d9kkZNiLz//MNy/aXdTbI4NcfmTJ87aR0ZNHFP073nde3snxgJXRU/IP78VXnZf9vf2igy4Bn1dXVnaOOOjnfP+EDOe/cz+fc867L5Mkr/kC7zTYT88vTPpVzzv5s9ttvlxzzX6evcPy/v3l2XrDrpFaWDUmSy297NPfOmJcLP/XCfOFNW+Wo0+5Y6bovnHZHjnrTVrnwUy/MvTPm5YrbH1127KGZ8/P7Ox7N+NFDl+076XdTssW4tXPmR3fLiR/YOV87e3IWLu7u9/OBJNnogD0zctJmOWfSK3Pt4Z/NC777//7m2isP/Ugu2PngXLDzwVkwY8m/60dvuC0X7npILtjxtbnvtIuy89c+2qLK4Skdk3ZNWW+jLPjv92bhWd/OkNf860rXdd1+TRZ875k/Mw/a6y3puvmKLDju37LwlK9m8GuO6O+SgV541qCilNJZSrm9FcXQd1dMvjGPznl8oMuAZ3XTTfdk0002zMSJG2TIkEF51YEvyKWX3rTCmt133yrDhw9Jkuy04+aZOnXmsmM333xvHnlkdvbYY5uW1g1JctnND+egF4xLKSU7bbZOHp+3ONNnLVhhzfRZC/LE/K7stNk6KaXkoBeMy6V/fnjZ8a+cOTkfec1zU/JUh0UpJXMWLE6tNXMXdGWdtQZnkGtgaZGND9o3d594ZpLkkWv+lCHrjsqwcRv0+vHTf3PNsi6LR66+MWtNGNcfZUKPOrfZPV03XpYkqVPuSIavnYwY/Yx1dcodyRMzn7E/qSnD1kqSlGFrp85+dCVrYMmMijXxq6meNaiotXYluaOUskkL6gHWUNOmzcy48U/94DB23LqZNm1lPzAscdppv8+ee26XJOnu7s5Xv3paPv6xQ/q9TliZabMWZNy6T3VCjFt36EqDirHrPLVm7DpDM23pmkv/PCNj1xmarTcescJjDn3Jxrlr2tzs+fkrc9DXrssnD35uOhr8QwNrlrU2Hpu5909dtj13ytSstfHYla7d/UdH54Abzsx2n1n5p81bHPaGPHjB5f1SJ/SkjFovddaMZdt11sMpo9br4RErWnTZz9O548sy7CM/yZB//kIWnfe9/igT6KPezqgYneSWUsq1SeY8ubPW+tq/9YBSyuFJDk+S7Ll5su2Gq1Am0E7OOvua3HzLffnZT49Mkpx00m+z517bZdy4Z35CAk03b2FXjr/k3nz/fTs949jvbn80W280Ij8+Yqfc9/C8HPa9P2XXLdbNiGFGSNEcVx76kcx7cHoGjVg7L/3lt7L5Px+Uu3961rLjmx362ozZdbtcstfbBrBK+PsM2mGvdP3xkiy+8ox0TNw6Qw75cBb8zxFJrQNdGrS13v4k9Nm+PnGt9fgkxydJef/u/kuHNjd27OhMfeipDoppUx/L2LHPDB6uvPK2fO97F+RnPz0yQ4YMTpLccONd+cMfJufkk36bOXMXZNGirqy19rB85MOva1n9tJ+f/25KTrvqoSTJdpuMzNTHnuqgmPrYgmy4XPdEkmy4XAdFsqQLY+w6Q3P/w/My5dH5OfiY65btP+Tr1+f/PvT8nH7tQ3nvvpumlJJNN1grE8YMy13T5maHTUe14AxpR5OO+Kc8971vSpI8ct2fs9bEpy7XWGvCuMx9YNozHjPvwelJksVPzMk9J52b9XbbYVlQMXbfF+V5n35fLtnrbeleuKgFZwBJ526vyqBdlwzk7n7gLynrPHXJUlln/dTHH+n9cz3/lVn4k88tea77b08GDUnWGpXMmbV6iwb6pFdBRa31t/1dCLBm2377TXPPvdNz/5SHM3bDdXPe+dfl6/912Aprbr31vnzu8z/P90/4YNZb76lf1JZfd/rpV+bmm+8VUtDvDn3JhBz6kglJkt/c8nBO+t0DOXDnDfOnex/PyOGDVhpUjBjWmRvvmZUdNx2Vs66bmkNfOiFbbjQiv//iS5at2/eoq3Lakc/P6BFDMn70sFx958zsusW6eXj2wtw9Y24mrjespedJe7nzuJNy53EnJUk2OnCvbPmBt+XeX5yX9V64YxbNmp35U2essL50dmbIuqOy4JGZKYMGZeNX752pl1yVJBm90zbZ7X+Pym/2f8+yAZvQCl3Xnpeua89LknRs+YIMeuGr0/Xn36ZM2CqZP+dvzKJYufrYjHRssVO6brgkZYOJKYMGCymgAXoVVJRSdk/y7STbJBmSpDPJnFqrj3wG2EnvPip7b7lL1h+xbu4/+ux8/twT8sMrzxnosuAZBg3qzOc+++a857Bvpau7O4cc8uJMmrRRvvmts7Pddptm3312zNeOOT1z5y7Iv//HCUmS8ePH5HvfNX2bgbfXtuvl8tsezX5fujrDhnTm6LdsvezY6465Lmd89AVJks8dsmU+efLtWbCoKy/dZr3suc2YHp/3iFdulk+edFte+7VrU2vy4VdvkdEjhvTrucCTHjz/t9nowL3ymsm/Stfcebn6XZ9aduyAG87MBTsfnI6hQ/Kyi76fMnhwSmdHpl1yVf56wilJkp2P+VgGjVgrLzn1m0mSOfc9lMsPev+AnAvtq/sv16VuuWuGfuj7y25P+qShR3w7C477YJJk0CvflUE77J0MHpphH/lJFv/hoiz+9UlZdOH3M/igf8ugFx+U1KzweFheh/tltlSpvbj+qpRyfZK3JDk1ya5J3p5ky1rrJ3v1Ii79YA1Qj/vyQJcAq0X3Bf830CXAKvvFq3490CXAavG6zzx3oEuA1WL4F89bo6dBTzj+dWvk77RTDj+jkX9vvc6Faq2Tk3TWWrtqrT9Ksn//lQUAAAC0o94O05xbShmS5MZSyteSPJQ+hBwAAAAAvdHboOKfsySY+ECSDyWZmOSQ/ioKAAAAmqKzNPIKiTVWb+/6cW8pZXiS8bXWL/RzTQAAAECb6tXlG6WU1yS5McmFS7d3KqWc3Y91AQAAAG2ot3Mm/l+S3ZI8liS11huTbN4vFQEAAABtq7czKhbVWmeVFa/LWSNvzwIAAADL6+wwo6KVeuyoKKWcX0rZPMktpZR/StJZSplUSvl2kitbUiEAAADQNp7t0o8fJbkoyT1JtkuyIMlJSWYl+fd+rQwAAABoOz0GFbXWU5PskmREklcl+b8kv0gyM8m/9nt1AAAAQFvpzYyKhUnmJBmaJYGF2RQAAAC0jc5iRkUr9RhUlFL2T3JskrOT7FJrnduSqgAAAIC29GwdFZ9O8sZa6y2tKAYAAABobz0GFbXWl7aqEAAAAIBnu+sHAAAAQMv0ZpgmAAAAtK1OH/G3lLcbAAAAaAxBBQAAANAYggoAAACgMcyoAAAAgB50ljLQJbQVHRUAAABAYwgqAAAAgMYQVAAAAACNYUYFAAAA9MCMitbSUQEAAAA0hqACAAAAaAxBBQAAALBSpZT9Syl3lFIml1I+sZLjm5RSfl1KuaGUclMp5cBVfU0zKgAAAKAHnR3tOaOilNKZ5DtJXpFkSpLrSiln11pvXW7ZZ5KcUmv9bill2yTnJ9lsVV5XRwUAAACwMrslmVxrvavWujDJL5Ic9LQ1Ncmopd+vk+TBVX1RQQUAAAC0oVLK4aWU65f7OvxpSzZOcv9y21OW7lve/0vytlLKlCzppvjgqtbl0g8AAABoQ7XW45Mcv4pP89YkP661fr2U8qIkPy2lbFdr7f57n1BHBQAAALAyDySZuNz2hKX7lndYklOSpNZ6VZJhSdZflRfVUQEAAAA96GzPWZpJcl2SSaWUzbMkoHhLkn962pr7kuyb5MellG2yJKiYsSovqqMCAAAAeIZa6+IkH0hyUZLbsuTuHreUUo4qpbx26bIPJ3lvKeVPSU5O8s5aa12V19VRAQAAAKxUrfX8LBmSufy+zy33/a1J9lidr6mjAgAAAGgMHRUAAADQg86O9h1SMRB0VAAAAACNIagAAAAAGkNQAQAAADSGGRUAAADQg85iRkUr6agAAAAAGkNQAQAAADSGoAIAAABoDDMqAAAAoAedHWZUtJKOCgAAAKAxBBUAAABAYwgqAAAAgMYQVAAAAACNYZgmAAAA9KDTLM2W0lEBAAAANIagAgAAAGgMQQUAAADQGGZUAAAAQA86OwypaCUdFQAAAEBjCCoAAACAxhBUAAAAAI1hRgUAAAD0oLOYUdFKOioAAACAxhBUAAAAAI0hqAAAAAAaw4wKAAAA6IEZFa2lowIAAABoDEEFAAAA0BiCCgAAAKAxBBUAAABAYximCQAAAD3o9BF/S3m7AQAAgMYQVAAAAACNIagAAAAAGsOMCgAAAOhBZykDXUJb0VEBAAAANIagAgAAAGgMQQUAAADQGGZUAAAAQA86O8yoaCUdFQAAAEBjCCoAAACAxhBUAAAAAI1hRgUAAAD0oLOYUdFKOioAAACAxhBUAAAAAI0hqAAAAAAaQ1ABAAAANIZhmgAAANCDTh/xt5S3GwAAAGgMQQUAAADQGIIKAAAAoDHMqAAAAIAedJYy0CW0FR0VAAAAQGMIKgAAAIDGEFQAAAAAjWFGBQAAAPSgs8OMilbSUQEAAAA0hqACAAAAaAxBBQAAANAYZlQAAABADzqLGRWtpKMCAAAAaAxBBQAAANAYggoAAACgMQQVAAAAQGMYpgkAAAA96PQRf0t5uwEAAIDGEFQAAAAAjSGoAAAAABqjJTMq6nFfbsXLQL8qR3xyoEuA1WL9Ldcf6BJglU2//o0DXQKsFt133DfQJQC90FnKQJfQVnRUAAAAAI0hqAAAAAAaQ1ABAAAANEZLZlQAAADAP6pOIypaSkcFAAAA0BiCCgAAAKAxBBUAAABAY5hRAQAAAD3oKIZUtJKOCgAAAKAxBBUAAABAYwgqAAAAgMYQVAAAAACNYZgmAAAA9KDTLM2W0lEBAAAANIagAgAAAGgMQQUAAADQGGZUAAAAQA86zKhoKR0VAAAAQGMIKgAAAIDGEFQAAAAAjWFGBQAAAPSg04yKltJRAQAAADSGoAIAAABoDEEFAAAA0BhmVAAAAEAPOjoMqWglHRUAAABAYwgqAAAAgMYQVAAAAACNIagAAAAAGsMwTQAAAOhBp1maLaWjAgAAAGgMQQUAAADQGIIKAAAAoDHMqAAAAIAedJhR0VI6KgAAAIDGEFQAAAAAjSGoAAAAABrDjAoAAADoQacZFS2lowIAAABoDEEFAAAA0BiCCgAAAKAxzKgAAACAHnQUQypaSUcFAAAA0BiCCgAAAKAxBBUAAABAY5hRAQAAAD3oNKKipXRUAAAAAI0hqAAAAAAaQ1ABAAAANIagAgAAAGgMwzQBAACgBx2GabaUjgoAAACgMQQVAAAAQGMIKgAAAIDGMKMCAAAAetBZDKloJR0VAAAAQGMIKgAAAIDGEFQAAAAAjWFGBQAAAPSgw4iKltJRAQAAADSGoAIAAABoDEEFAAAA0BhmVAAAAEAPOs2oaCkdFQAAAMBKlVL2L6XcUUqZXEr5xN9Y86ZSyq2llFtKKSet6mvqqAAAAACeoZTSmeQ7SV6RZEqS60opZ9dab11uzaQkn0yyR611Zillw1V9XR0VAAAAwMrslmRyrfWuWuvCJL9IctDT1rw3yXdqrTOTpNY6fVVfVFABAAAArMzGSe5fbnvK0n3L2zLJlqWU35dSri6l7L+qL+rSDwAAAOhBxxr6EX8p5fAkhy+36/ha6/F9fJpBSSYl2TvJhCSXl1K2r7U+9vfWJagAAACANrQ0lOgpmHggycTltics3be8KUmuqbUuSnJ3KeUvWRJcXPf31rWG5kIAAADAKrouyaRSyuallCFJ3pLk7KetOTNLuilSSlk/Sy4FuWtVXlRQAQAAADxDrXVxkg8kuSjJbUlOqbXeUko5qpTy2qXLLkrySCnl1iS/TvLRWusjq/K6Lv0AAACAHnSWMtAlDJha6/lJzn/avs8t931NcuTSr9VCRwUAAADQGIIKAAAAoDEEFQAAAEBjmFEBAAAAPeho3xEVA0JHBQAAANAYggoAAACgMQQVAAAAQGOYUQEAAAA96DSjoqV0VAAAAACNIagAAAAAGkNQAQAAADSGoAIAAABoDMM0AQAAoAcdhmm2lI4KAAAAoDEEFQAAAEBjCCoAAACAxjCjAgAAAHrQWQypaCUdFQAAAEBjCCoAAACAxhBUAAAAAI1hRgUAAAD0oMOIipbSUQEAAAA0hqACAAAAaAxBBQAAANAYZlQAAABADzrNqGgpHRUAAABAYwgqAAAAgMYQVAAAAACNIagAAAAAGsMwTQAAAOhBRzFNs5V0VAAAAACNoaPiH8DlV9ySL33plHR3d+eNb9gjhx++/wrHf/SjS3Lqab9LZ2dnxowZkaO/9PZsvPF6y44/8cS8HPiqL+Tl++6Yz33ura0uH3rlB//86bx6+z0yffbMbP/FQwe6HPib9tl0l3xp78PT2dGRn918cb513WkrHN945Ab5n/0+lHWGrp2O0pH//N1Pcsk912dQR2f++xX/lu033CKDSmdOue2yfPO6UwfoLGhHV/xpar504g3p7q55w8uek8Nfu/UKxxcu6srHv3ttbrl7ZtYdMTTH/tvumbDB2vn9n6fl6yfflEVd3Rnc2ZGPHbpjdn/ehkmS86+6P98787Z0d9fsvcv4fOStOwzEqdFmaq05+sJ7c/mdj2X44I4cffAW2Xb82s9Yd8uDc/Kps/6a+Yu6s+ekdfOp/TdNKSW3TZ2TL5x7dxYsrhnUUfLZV22WHTYekdnzF+fjZ/w1D81amMXdNe960fi8fucNBuAMAR0VDdfV1Z2jjjo53z/hAznv3M/n3POuy+TJD66wZpttJuaXp30q55z92ey33y455r9OX+H4f3/z7Lxg10mtLBv67MdXnZf9v/2hgS4DetRROvKVfd6ft5z5+ezxkyPyuq32ypZjJq6w5sgXvjln/eWK7PPzf8/h538tX93n/UmS1056SYZ0Ds5eP/1AXn7Sf+Tt2++fiaM2HIjToA11ddcc9aM/5oSPvTTnHrN/zrvyvkye8vgKa077zd0ZtfaQXPyNA/OOAybl6yfflCQZPXJIvvvRl+Scr+6Xr7x/t3zsuGuSJDNnL8gxJ/0pP/70Xjn3mP0y47H5uermaS0/N9rP5ZNn5d5H5+fCD+6YL7xm83zhvLtXuu6o8+7OUa/ZPBd+cMfc++j8XDF5VpLk67+6L0fsNSFnvG/7fOBlE/L1X92XJDnpumnZYv3hOeN92+cn79gmX7v43izs6m7ZeQFPEVQ03E033ZNNN9kwEydukCFDBuVVB74gl1560wprdt99qwwfPiRJstOOm2fq1JnLjt1887155JHZ2WOPbVpaN/TVFZNvzKNzHn/2hTCAdhm3Ze557KHcO2taFnUvzpl3XJ4Dtth9hTW11owcslaSZNTQtTN1zqNL9qdmrcHD0lk6MmzQkCzqXpzZC+a2/BxoTzdNfjSbjB2RiWNHZMigjhz4oom59A8PrLDm0usfzMEv3SxJst8LJ+Sqm6en1pptNxudsaOHJ0kmTRiVBQu7snBRV6ZMn5NNx43MmFFDkyQv3m5sLr52xeeE/nDZ7TNz0A7rp5SSHSeMzOz5XZkxe+EKa2bMXpgnFnRlxwkjU0rJQTusn0tvX/IzciklcxZ0JUmemL84G45c8nN0STJnYVdqrZm7sCvrDB+UQR3mErBEZ1kzv5rKpR8NN23azIwbP3rZ9thx6+amP608NU6S0077ffbcc7skSXd3d7761dNyzDHvzpVX3tbvtQKs6caPWC8PzJ6xbPvBJx7O88dttcKaY64+Kae8/ot5z06vyVqDh+WQX346SXLOnb/PAVvsnpsP/2mGDx6az/72hDy24ImW1k/7mjZzXsavt9ay7XFj1sqfJj+ywprpM+dl/HpLAolBnR0ZudbgPDZ7YUYvDSKS5KJrH8i2m43OkMGd2WTsiNz90OxMmTEn48YMzyXXP5BFi336TP+bPnthxq3z1L/LsaOGZNrshdlgaeCQJNNmL8zYUUNWWDN9aZjxif02zXt/dnuO+dV96a41P3/385Ikh+42Lv/6izuy17E3ZM6Crhz7hucaoAgDpNdBRSllrSQfTrJJrfW9pZRJSbaqtZ7bb9XRJ2edfU1uvuW+/OynRyZJTjrpt9lzr+0ybtzoZ3kkAKvL67baK7+45dJ8949nZNfxW+e4/T+cl574r9ll3Jbp6u7O9ie8PesOHZFz3vTVXH7fjbl3llZ5/jHcOWVWvn7yTfnBJ/dMkqwzYkg+/65dcuS3rk4pyc5brp/7pwnfaL5fXD8tn9hv07xy2zG54JZH8tmz78oP375NfvfXx7L12LXzo7dvk/tmLsh7fnp7nr/pyIwY6rNdaLW+/Ff3oyR/SPKipdsPJDk1yUqDilLK4UkOT5L//d6ROfzwV69Cme1r7NjRmfrQU5dyTJv6WMaOfWbwcOWVt+V737sgP/vpkRkyZHCS5IYb78of/jA5J5/028yZuyCLFnVlrbWH5SMffl3L6gdYkzz0xCPZeORTg9U2GrF+HnpixU+lD93uFXnz6Z9Pklz/0O0ZOmhI1hs+KodstVcuu/cPWdzdlYfnzcq1D96WncZOElTQEmNHD89Djzx1qdHUR+dm7JjhK6zZcPTwPPTIvIxbb60s7urO7LmLsu7ST6inPjI3Hzj2ynz1/btlk7Ejlj1mn+dvlH2ev1GS5P8uvSud2uTpJyddOzWn/nFJR9v2G62dqbMWJBmZJJn2+MKMXa6bIknGjhySaY8/dTnItMcXLrvE46w/PZxP7b9pkmT/bcfkc2fflSQ548aH8549xqeUkk3HDMuEdYfmrofnZ4eNRwRorb7MqNii1vq1JIuSpNY6N0su5VqpWuvxtdZda627Cin+fttvv2nuuXd67p/ycBYuXJzzzr8u++yz4kTtW2+9L5/7/M/z3ePen/XWG7Vs/9f/67D85tdfzmWXHZ2Pf+yQHHzQC4UUAKvghql/yeajN8omo8ZmcMegHLzVnrnwrmtWWPPA4zOy5yY7JkkmjZmQYZ2D8/C8WZkye0ZeOnHJ/7/XGjQ0zx+/Ve58dErLz4H2tP0Wo3Pv1CcyZfqcLFzcnfOvun9ZwPCkfZ6/Uc684p4kyUXXTMnuz9swpZQ8Pmdh/uWY3+XDb9k+u2y1/gqPeWTW/CTJrCcW5uRLJucNL9u8JedD+/mn3cbljPdtnzPet3323Xp0zrrp4dRa86cpszNyaOcKl30kyQYjh2TE0M78acrs1Fpz1k0PZ5+tl3zYt+HIwbnu3tlJkqvvfjybrjcsSTJ+1JBcffeSeVkPP7Eodz8yLxNHDw0kSUcpa+RXU/Wlo2JhKWV4kpokpZQtkizol6pYZtCgznzus2/Oew77Vrq6u3PIIS/OpEkb5ZvfOjvbbbdp9t1nx3ztmNMzd+6C/Pt/nJAkGT9+TL733SMGuHLom5PefVT23nKXrD9i3dx/9Nn5/Lkn5IdXnjPQZcEKump3PnnZ93LK649KR+nIybf8Knc8cl8+/qJDc+O0O3PRXdfmc5f/IN94xQfzL7scnNSaD17030mSH/7pvHzrlf+RK97+nZSUnHzLJbn14XsG8nRoI4M6O/LZd+6cw75yebq7aw7Ze/NMmrBOvnXqzdnuOWOyz/M3yhv23jwfO+7avPJD52edtYfk2A8uGRT784sn575pT+S4M27NcWfcmiT5wSf2zHrrDMuXTrwxd9z3WJLkiNdtm83HjxyoU6SN7Dlp3Vx+52PZ/9t/yrDBHfnSQc9Zdux13/tzznjf9kmSz75qs3zqzLuyYHF3XvrcdbPnc9dJknzhNc/Jly+8J13dyZBBJV949ZLHv3+vjfOpM/+ag757U2pNjnz5Jhm91uDWnyCQUmvt3cJSXpHkM0m2TXJxkj2SvLPW+ptnfXD9de9eBBqsHPHJgS4BVov1t1z/2RdBw03fc6eBLgFWi+477hvoEmC16PynE5v78fxq8Iu/fGCN/J32LVv+TyP/3nrdUVFr/VUp5Y9Jds+SSz7+vdb6cL9VBgAAALSdvtz143VJLqu1nrd0e91SysG11jP7qzgAAAAYaE2e57Am6sswzc/XWmc9uVFrfSzJ51d7RQAAAEDb6ktQsbK1bioMAAAArDZ9CSquL6UcW0rZYunXsUn+0F+FAQAAAO2nL0HFB5MsTPJ/S78WJPnX/igKAAAAaE99uevHnCSf6MdaAAAAoHEM02ytZw0qSin/XWv9j1LKOUmece/YWutr+6UyAAAAoO30pqPip0v//K/+LAQAAADgWYOKWusfSimdSQ6vtR7agpoAAACANtWrGRW11q5SyqallCG11oX9XRQAAAA0RUfpy30oWFW9HqaZ5K4kvy+lnJ1kzpM7a63HrvaqAAAAgLbUl6Dir0u/OpKM7J9yAAAAgHbWq6CilLJTkluS3FJrva1fKwIAAADaVm9uT/q5JG9L8ockXyulfLnWekK/VwYAAAAN0FHKQJfQVnrTUfHmJDvVWueWUtZLcmESQQUAAACw2vVmdOmCWuvcJKm1PtLLxwAAAAD0WW86Kp6z9E4fSVKSbLHcdmqtr+2XygAAAIC205ug4qCnbf9XfxQCAAAATWRGRWs9a1BRa/1tb56olPLLWushq14SAAAA0K5W57yJ56zG5wIAAADa0OoMKupqfC4AAACgDbmDBwAAANAYvRmm2VumiwAAALDGMUyztVZnR8XHV+NzAQAAAG2o1x0VpZQ/55lzKGYluT7Jf9ZaL16dhQEAAADtpy+XflyQpCvJSUu335JkrSRTk/w4yWtWa2UAAABA2+lLUPHyWusuy23/uZTyx1rrLqWUt63uwgAAAKAJOtyHoqX68m53llJ2e3KjlPKCJJ1LNxev1qoAAACAttSXjor3JPlhKWVEltzh4/Ek7ymlrJ3ky/1RHAAAANBeeh1U1FqvS7J9KWWdpduzljt8yuouDAAAAGg/fbnrx9AkhyTZLMmgsvQ+srXWo/qlMgAAAGiAjqW//9Iafbn046wsuR3pH5Is6J9yAAAAgHbWl6BiQq11/36rBAAAAGh7fbnrx5WllO37rRIAAACg7fWlo+IlSd5ZSrk7Sy79KElqrXWHfqkMAAAAGsCMitbqS1BxQL9VAQAAAJBeBBWllFG11seTzG5BPQAAAEAb601HxUlJXp0ld/uoWXLJx5Nqkuf0Q10AAABAG3rWoKLW+uqlf27e/+UAAAAA7aw3l37s0tPxWusfV185AAAA0CwdpS83zGRV9ebSj6/3cKwm2Wc11QIAAAC0ud5c+vGyVhQCAAAA0JtLP17f0/Fa6+mrrxwAAACgnfXm0o/X9HCsJhFUAAAAsMbqKOXZF7Ha9ObSj3e1ohAAAACAXo8uLaWMLaX8oJRywdLtbUsph/VfaQAAAEC76cs9Vn6c5KIkGy3d/kuS/1jN9QAAAABtrDczKp60fq31lFLKJ5Ok1rq4lNLVT3UBAABAI5hR0Vp96aiYU0pZL0sGaKaUsnuSWf1SFQAAANCW+tJRcWSSs5NsUUr5fZINkryhX6oCAAAA2tKzdlSUUl5QShlXa/1jkr2SfCrJgiQXJ5nSz/UBAAAAbaQ3HRX/m+TlS79/cZJPJ/lgkp2SHB9dFQAAAKzBzKhord4EFZ211keXfv/mJMfXWn+Z5JellBv7rTIAAACg7fRmmGZnKeXJQGPfJJctd6wvMy4AAAAAetSboOHkJL8tpTycZF6SK5KklPLcuOsHAAAAsBo9a1BRa/1SKeXSJOOTXFxrrUsPdWTJrAoAAACA1aJXl27UWq9eyb6/rP5yAAAAoFk6Sm+mJrC6eLcBAACAxhBUAAAAAI0hqAAAAAAaw+1FAQAAoAcdKQNdQlvRUQEAAAA0hqACAAAAaAxBBQAAANAYZlQAAABADzqKGRWtpKMCAAAAaAxBBQAAANAYggoAAACgMcyoAAAAgB50FJ/xt5J3GwAAAGgMQQUAAADQGIIKAAAAoDEEFQAAAEBjGKYJAAAAPegoZaBLaCs6KgAAAIDGEFQAAAAAjSGoAAAAABrDjAoAAADogRkVraWjAgAAAGgMQQUAAADQGIIKAAAAoDHMqAAAAIAedBSf8beSdxsAAABoDEEFAAAA0BiCCgAAAKAxzKgAAACAHnSUMtAltBUdFQAAAEBjCCoAAACAxhBUAAAAAI0hqAAAAAAawzBNAAAA6EFHDNNsJR0VAAAAQGMIKgAAAIDGEFQAAAAAK1VK2b+UckcpZXIp5RM9rDuklFJLKbuu6muaUQEAAAA96CjtOaOilNKZ5DtJXpFkSpLrSiln11pvfdq6kUn+Pck1q+N1dVQAAAAAK7Nbksm11rtqrQuT/CLJQStZ98UkX00yf3W8qKACAAAAWJmNk9y/3PaUpfuWKaXskmRirfW81fWiggoAAABoQ6WUw0sp1y/3dXgfH9+R5NgkH16ddZlRAQAAAD3oKGvmZ/y11uOTHN/DkgeSTFxue8LSfU8amWS7JL8pS+Z4jEtydinltbXW6//eutbMdxsAAABYVdclmVRK2byUMiTJW5Kc/eTBWuusWuv6tdbNaq2bJbk6ySqFFImgAgAAAFiJWuviJB9IclGS25KcUmu9pZRyVCnltf31ui79AAAAAFaq1np+kvOftu9zf2Pt3qvjNQUVAAAA0IOOJfMXaJGWBBXdF/xfK14G+tX6W64/0CXAavHwXx4e6BJglZUjXjTQJcBqURYtGugSABrHjAoAAACgMQQVAAAAQGMIKgAAAIDGMEwTAAAAelCKz/hbybsNAAAANIagAgAAAGgMQQUAAADQGGZUAAAAQA86fMbfUt5tAAAAoDEEFQAAAEBjCCoAAACAxjCjAgAAAHpQis/4W8m7DQAAADSGoAIAAABoDEEFAAAA0BhmVAAAAEAPOsyoaCnvNgAAANAYggoAAACgMQQVAAAAQGMIKgAAAIDGMEwTAAAAelB8xt9S3m0AAACgMQQVAAAAQGMIKgAAAIDGMKMCAAAAetBRfMbfSt5tAAAAoDEEFQAAAEBjCCoAAACAxjCjAgAAAHpQfMbfUt5tAAAAoDEEFQAAAEBjCCoAAACAxjCjAgAAAHrQUXzG30rebQAAAKAxBBUAAABAYwgqAAAAgMYQVAAAAACNYZgmAAAA9KAYptlS3m0AAACgMQQVAAAAQGMIKgAAAIDGMKMCAAAAetDhM/6W8m4DAAAAjSGoAAAAABpDUAEAAAA0hhkVAAAA0INSfMbfSt5tAAAAoDEEFQAAAEBjCCoAAACAxjCjAgAAAHrQYUZFS3m3AQAAgMYQVAAAAACNIagAAAAAGkNQAQAAADSGYZoAAADQg5LOgS6hreioAAAAABpDUAEAAAA0hqACAAAAaAwzKgAAAKAHHcVn/K3k3QYAAAAaQ1ABAAAANIagAgAAAGgMMyoAAACgB8Vn/C3l3QYAAAAaQ1ABAAAANIagAgAAAGgMMyoAAACgBx3FZ/yt5N0GAAAAGkNQAQAAADSGoAIAAABoDEEFAAAA0BiGaQIAAEAPimGaLeXdBgAAABpDUAEAAAA0hqACAAAAaAwzKgAAAKAHHT7jbynvNgAAANAYggoAAACgMQQVAAAAQGOYUQEAAAA9KMVn/K3k3QYAAAAaQ1ABAAAANIagAgAAAGgMMyoAAACgBx1mVLSUdxsAAABoDEEFAAAA0BiCCgAAAKAxBBUAAABAYximCQAAAD0oPuNvKe82AAAA0BiCCgAAAKAxBBUAAABAY5hRAQAAAD3oKD7jbyXvNgAAANAYggoAAACgMQQVAAAAQGOYUQEAAAA9KD7jbynvNgAAANAYggoAAACgMQQVAAAAQGOYUQEAAAA96Cg+428l7zYAAADQGIIKAAAAoDEEFQAAAEBjmFHRULXWHH3Gnbn8tkczbHBHjn7rNnnexJHPWHfL/bPzyZNvy4JF3dlzmzH51OsmpZSy7PiPfn1fvnb2X3PlF/fI6BFDMnve4nzsZ7fmocfmZ3FXzbtftkle/8LxrTw12tg+m+6SL+19eDo7OvKzmy/Ot647bYXjG4/cIP+z34eyztC101E68p+/+0kuuef6DOrozH+/4t+y/YZbZFDpzCm3XZZvXnfqAJ0F/G0/+OdP59Xb75Hps2dm+y8eOtDlQK9d/rvb8qWvnpnu7u688fW75/DD9l3h+I9O/E1OPf2adHZ2ZMzoETn6qDdn443GDFC1tKMrbpqWo3/+53R317xhr03z3ldvucLxhYu68vHj/5hb73ks644YkmOP2DUbb7B2kuT4c/6SX15+bzo6Sj79tu3zku3HJkl+fOHknPbbe1NKsuWEUTn6Pbtk6JDO/PxXd+XEi/+a+6bPyZX/c0BGjxza8vOFdqejoqEuv+3R3DtjXi781AvzhTdtlaNOu2Ol675w2h056k1b5cJPvTD3zpiXK25/dNmxh2bOz+/veDTjRz/1P9eTfjclW4xbO2d+dLec+IGd87WzJ2fh4u5+Px/oKB35yj7vz1vO/Hz2+MkRed1We2XLMRNXWHPkC9+cs/5yRfb5+b/n8PO/lq/u8/4kyWsnvSRDOgdnr59+IC8/6T/y9u33z8RRGw7EaUCPfnzVedn/2x8a6DKgT7q6unPU0afn+989POed+fGce8EfM/mvU1dYs83WG+eXJ38o5/zyo9nvFTvkmG+cO0DV0o66umu+eOKfcvyHX5Rzvrxvzrt6SiY/8PgKa067/N6ss/bgXHTMK/L2/bbIf51ya5Jk8gOP5/xrpuSco/fJCR95UY76yZ/S1V0z7dF5+dmv7sppX9g75xy9b7q7a86/ZkqSZOctx+SHH3txNlp/eKtPlQYrpWON/Gqq5lbW5i67+eEc9IJxKaVkp83WyePzFmf6rAUrrJk+a0GemN+VnTZbJ6WUHPSCcbn0zw8vO/6VMyfnI695bkqe6rAopWTOgsWptWbugq6ss9bgDOoogf62y7gtc89jD+XeWdOyqHtxzrzj8hywxe4rrKm1ZuSQtZIko4aunalzlgRvNTVrDR6WztKRYYOGZFH34sxeMLfl5wDP5orJN+bROY8/+0JokJtuvi+bbrJ+Jk5YL0MGD8qr9t85l/765hXW7L7bpAwfPiRJstMOm2bqtMcGoFLa1U13zcwmY0dk4oZrZ8igjhz4wgm57I8rhmmX/XFqDnrJJkmS/V6wUa6+dUZqrbnsj1Nz4AsnZMjgzkzYYO1sMnZEbrprZpIlAcj8hV1Z3NWdeQu7suG6S4KJbTddd1k3BjAw+nTpRynlJUkm1Vp/VErZIMmIWuvd/VNae5s2a0HGrftUJ8S4dYdm+qwF2XCdp/ZNn7UgY5fbHrvO0ExbGmZc+ucZGbvO0Gy98YgVnvfQl2ycI37w5+z5+Sszd0FXvv72bdMhqKAFxo9YLw/MnrFs+8EnHs7zx221wppjrj4pp7z+i3nPTq/JWoOH5ZBffjpJcs6dv88BW+yemw//aYYPHprP/vaEPLbgiZbWD7CmmjZtVsaNXXfZ9tix6+amP9/7N9efdsY12fMl27SgMlhi+sx5GTfmqe6GsWOG5aa/zlxhzbSZ8zJ+6ZpBnR0ZOXxQHntiYabNnJcdtxizwmOnz5yXnZ87Ju864LnZ98iLMnRIZ/bYbsPssb1uTWiKXndUlFI+n+TjST65dNfgJD/rYf3hpZTrSynXH3/BratWJX0yb2FXjr/k3nzwgM2fcex3tz+arTcakcu/8OKc/pFd85+n35kn5i8egCrhmV631V75xS2XZsfvvzNvPfP/5bj9P5ySkl3GbZmu7u5sf8Lbs+sPDssRu7wum64zdqDLBWg7Z517fW6+5f68550vG+hSYJXMmrMwl/3xofzqv16Z3/73/pm3YHHO/v39A10WsFRfLv14XZLXJpmTJLXWB5M8c7rjUrXW42utu9Zadz38gG1Xrco28fPfTcnrjrkurzvmumwwakimPvbUpR5TH1uxmyJJNlyugyJZ0oUxdp2huf/heZny6PwcfMx12feoqzJt1oIc8vXrM+PxBTn92ofyih02SCklm26wViaMGZa7pmmhp/899MQj2XjkBsu2Nxqxfh564pEV1hy63Sty1l+uSJJc/9DtGTpoSNYbPiqHbLVXLrv3D1nc3ZWH583KtQ/elp3GTmpp/QBrqrFj11nhUo5p0x7L2A3Xeca6K6/+S753wiX57rcOy5Ah5rHTOhuOHp6pj85btj3t0fkZO3rF+RFjRw/PQ0vXLO7qzux5i7PuiCEZu5LHbjh6eK66ZUY23mCtjBk1NIMHdeTlz98oN0x+NPC3lLpmfjVVX4KKhbXWmqQmSSnFhVur2aEvmZAzPvqCnPHRF2Tf7dbPWddNTa01N94zKyOHD1ppUDFiWGduvGdWaq0567qp2We79bPlRiPy+y++JJd+7kW59HMvyth1huaXH941G4wamvGjh+XqO5e0yj08e2HunjE3E9cbNhCnS5u5YepfsvnojbLJqLEZ3DEoB2+1Zy6865oV1jzw+IzsucmOSZJJYyZkWOfgPDxvVqbMnpGXTtwhSbLWoKF5/vitcuejU1p+DgBrou2fNzH33Dsj9095JAsXLc55F96QffbeboU1t942JZ876tR891uHZb31/ubnVNAvtt983dw77YlMmTEnCxd35/xrpuRlO49bYc3Ldh6Xs353X5LkousezO7brJ9SSl6287icf82ULFzUlSkz5uTeaU9kh+eMzvj1hudPk2dm3tLZbVffOiNbbDRiZS8PDICyJHvoxcJSPpJkUpJXJPlykncnOanW+u1ne2z3+e9rcFbTTLXWfPGXd+Z3tz+SYUM6c/Rbts52m4xKkrzumOtyxkdfkCS5+b7H88mTb8+CRV156Tbr5TOvX/H2pEmy71FX5bQjn5/RI4Zk+qwF+eRJt2XG7IWpNXnvvpvktbuOe8br80xj7/CL8ap6+Wa75j/3fm86SkdOvuVX+ca1p+TjLzo0N067MxfddW22HDMx33jFB7PW4OFJrfnCFT/Kb+67IWsPHpZvvfI/suV6E1NScvItl+Q7fzh9oE/nH9bDf3n42Rfxdznp3Udl7y13yfoj1s20xx/N5889IT+88pyBLmuNVP/7swNdwhrlt1fcmqO/dla6urpzyMG75f2HvyLf/M4F2W7bidn3Zdvlne/9bv5y50PZYIMlP4uMHzc63/v2YQNc9Zqh+4bLB7qEfwi//dPUfHnp7Ulfv+emed9rt8q3Tr8t2222bvbZZXwWLOzKx4//Q267d1bWWXtwvn7ECzJxwyWfq37v7Dty+uX3prOzI5/8p+2z545LLh/99um35YJrH0hnR8k2m66T/3z3zhkyuDM/vfiv+cH5d+bhWQsyZtTQ7LnD2PznYTsP5On/Q+jY/atr9uC7+us183fa8rJG/r31OqhIklLKK5K8MklJclGt9Ve9eZyggjWBoII1haCCNYGggjWFoII1haDiH1RDg4peX2BYStk8yRVPhhOllOGllM1qrff0V3EAAAAw4Gr3QFfQPxoZU/RtRsWpSZb/2+laug8AAABgtehLUDGo1rrwyY2l3w9Z/SUBAAAA7aovQcWMUsprn9wopRyUxIXOAAAAwGrTl5tgvy/Jz0sp/5MlV7Lcn+Tt/VIVAAAANMWaOqOioXodVNRa/5pk91LKiKXbT/RbVQAAAEBbetagopTytlrrz0opRz5tf5Kk1npsP9UGAAAAtJnedFSsvfTPkf1ZCAAAAMCzBhW11v8tpXQmebzW+o0W1AQAAAC0qV7NqKi1dpVS3ppEUAEAAEB7MUyzpfpy14/fL73jx/8lmfPkzlrrH1d7VQAAAEBb6ktQsdPSP49abl9Nss9qqwYAAABoa30JKt5Ya3243yoBAAAA2l5vbk/6miQ/TLKolNKd5E211iv7vTIAAABoAjMqWqqjF2u+lOSltdaNkhyS5Mv9WxIAAADQrnoTVCyutd6eJLXWa5KM7N+SAAAAgHbVmxkVG5ZSjvxb27XWY1d/WQAAAEA76k1QcUJW7KJ4+jYAAACsubrNqGilZw0qaq1f6M0TlVI+WWs1vwIAAAD4u/VmRkVvvXE1PhcAAAAwwEop+5dS7iilTC6lfGIlx48spdxaSrmplHJpKWXTVX3N1RlUlNX4XAAAAMAAKqV0JvlOkgOSbJvkraWUbZ+27IYku9Zad0hyWpKvrerr9mZGRW/V1fhcAAAA0Ay1bWdU7JZkcq31riQppfwiyUFJbn1yQa3118utvzrJ21b1RXVUAAAAQBsqpRxeSrl+ua/Dn7Zk4yT3L7c9Zem+v+WwJBesal297qgopexRa/19D/tOXdViAAAAgNaotR6f5PjV8VyllLcl2TXJXqv6XH3pqPh2T/tqrUevajEAAABAYzyQZOJy2xOW7ltBKeXlST6d5LW11gWr+qLP2lFRSnlRkhcn2aCUcuRyh0Yl6VzVAgAAAIBGui7JpFLK5lkSULwlyT8tv6CUsnOS/02yf611+up40d5c+jEkyYila0cut//xJG9YHUUAAABAY7XpMM1a6+JSygeSXJQljQo/rLXeUko5Ksn1tdazkxyTJZnBqaWUJLmv1vraVXndZw0qaq2/TfLbUsqPa633rsqLAQAAAP84aq3nJzn/afs+t9z3L1/dr9mX25MOLaUcn2Sz5R9Xa91ndRcFAAAAtKe+BBWnJvleku8n6eqfcgAAAIB21pegYnGt9bv9VgkAAAA0UZvOqBgofbk96TmllCNKKeNLKWOe/Oq3ygAAAIC205eOincs/fOjy+2rSZ6z+soBAAAA2lmvg4pa6+b9WQgAAABAr4OKUspaSY5Mskmt9fBSyqQkW9Vaz+236gAAAGCgdZtR0Up9mVHxoyQLk7x46fYDSf5ztVcEAAAAtK2+BBVb1Fq/lmRRktRa5yYp/VIVAAAA0Jb6ElQsLKUMz5IBmimlbJFkQb9UBQAAALSlvtz14/NJLkwysZTy8yR7JHlnfxQFAAAAjVHNqGilvtz141ellD8m2T1LLvn491rrw/1WGQAAANB2en3pRylljyTza63nJVk3yadKKZv2V2EAAABA++nLjIrvJplbStkxS25T+tckJ/ZLVQAAAEBb6ktQsbjWWpMclOQ7tdbvJBnZP2UBAAAA7agvwzRnl1I+meSfk7y0lNKRZHD/lAUAAAANYZhmS/Wlo+LNWXI70nfXWqcmmZDkmH6pCgAAAGhLvQ4qloYTv0wydOmuh5Oc0R9FAQAAAO2pL3f9eG+S05L879JdGyc5sx9qAgAAANpUX2ZU/GuS3ZJckyS11jtLKRv2S1UAAADQFGZUtFRfZlQsqLUufHKjlDIoSV39JQEAAADtqi9BxW9LKZ9KMryU8ookpyY5p3/KAgAAANpRX4KKjyeZkeTPSf4lyflJPtMfRQEAAADtqVczKkopnUluqbVuneSE/i0JAAAAmqPWroEuoV+UgS7gb+hVR0Vd8rdyRyllk36uBwAAAGhjfbnrx+gkt5RSrk0y58mdtdbXrvaqAAAAgLbUl6Dis/1WBQAAAEB6EVSUUoYleV+S52bJIM0f1FoX93dhAAAA0Ajd3QNdQVvpzYyKnyTZNUtCigOSfL1fKwIAAADaVm8u/di21rp9kpRSfpDk2v4tCQAAAGhXvemoWPTkNy75AAAAAPpTbzoqdiylPL70+5Jk+NLtkqTWWkf1W3UAAAAw0KoZFa30rEFFrbWzFYUAAAAA9ObSDwAAAICWEFQAAAAAjSGoAAAAABqjN8M0AQAAoH0ZptlSOioAAACAxhBUAAAAAI0hqAAAAAAaw4wKAAAA6IkZFS2lowIAAABoDEEFAAAA0BiCCgAAAKAxzKgAAACAnphR0VI6KgAAAIDGEFQAAAAAjSGoAAAAABrDjAoAAADoSbcZFa2kowIAAABoDEEFAAAA0BiCCgAAAKAxBBUAAABAYximCQAAAD2phmm2ko4KAAAAoDEEFQAAAEBjCCoAAACAxjCjAgAAAHpiRkVL6agAAAAAGkNQAQAAADSGoAIAAABoDDMqAAAAoCdmVLSUjgoAAACgMQQVAAAAQGMIKgAAAIDGMKMCAAAAetJtRkUr6agAAAAAGkNQAQAAADSGoAIAAABoDEEFAAAA0BiGaQIAAEBPqmGaraSjAgAAAGgMQQUAAADQGIIKAAAAoDHMqAAAAICemFHRUjoqAAAAgMZoSUfFL17161a8DPSr6de/caBLgNWiHPGigS4BVln5jy8OdAmwWnR/8k0DXQJA4+ioAAAAABrDjAoAAADoSbcZFa2kowIAAABoDEEFAAAA0BiCCgAAAKAxzKgAAACAnnTXga6greioAAAAABpDUAEAAAA0hqACAAAAaAxBBQAAANAYhmkCAABAT7q7B7qCtqKjAgAAAGgMQQUAAADQGIIKAAAAoDHMqAAAAICemFHRUjoqAAAAgMYQVAAAAACNIagAAAAAGsOMCgAAAOhJdx3oCtqKjgoAAACgMQQVAAAAQGMIKgAAAIDGMKMCAAAAetLdPdAVtBUdFQAAAEBjCCoAAACAxhBUAAAAAI0hqAAAAAAawzBNAAAA6Ilhmi2lowIAAABoDEEFAAAA0BiCCgAAAKAxzKgAAACAnnTXga6greioAAAAABpDUAEAAAA0hqACAAAAaAwzKgAAAKAn3d0DXUFb0VEBAAAANIagAgAAAGgMQQUAAADQGGZUAAAAQE+660BX0FZ0VAAAAACNIagAAAAAGkNQAQAAADSGoAIAAABoDMM0AQAAoCfd3QNdQVvRUQEAAAA0hqACAAAAaAxBBQAAANAYZlQAAABAT8yoaCkdFQAAAEBjCCoAAACAxhBUAAAAAI1hRgUAAAD0oNY60CX0izLQBfwNOioAAACAxhBUAAAAAI0hqAAAAAAaw4wKAAAA6El390BXMGBKKfsn+WaSziTfr7V+5WnHhyY5McnzkzyS5M211ntW5TV1VAAAAADPUErpTPKdJAck2TbJW0sp2z5t2WFJZtZan5vkG0m+uqqvK6gAAAAAVma3JJNrrXfVWhcm+UWSg5625qAkP1n6/WlJ9i2lrNINRQQVAAAAwMpsnOT+5banLN230jW11sVJZiVZb1VeVFABAAAAbaiUcngp5frlvg4f6JoSwzQBAACgZ2voMM1a6/FJju9hyQNJJi63PWHpvpWtmVJKGZRknSwZqvl301EBAAAArMx1SSaVUjYvpQxJ8pYkZz9tzdlJ3rH0+zckuazWWlflRXVUAAAAAM9Qa11cSvlAkouy5PakP6y13lJKOSrJ9bXWs5P8IMlPSymTkzyaJWHGKhFUAAAAACtVaz0/yflP2/e55b6fn+SNq/M1BRUAAADQk+5VupKBPjKjAgAAAGgMQQUAAADQGIIKAAAAoDHMqAAAAICedHcPdAVtRUcFAAAA0BiCCgAAAKAxBBUAAABAY5hRAQAAAD0xo6KldFQAAAAAjSGoAAAAABpDUAEAAAA0hqACAAAAaAzDNAEAAKAn3XWgK2grOioAAACAxhBUAAAAAI0hqAAAAAAaw4wKAAAA6El390BX0FZ0VAAAAACNIagAAAAAGkNQAQAAADSGGRUAAADQEzMqWkpHBQAAANAYggoAAACgMQQVAAAAQGOYUQEAAAA96a4DXUFb0VEBAAAANIagAgAAAGgMQQUAAADQGIIKAAAAoDEM0wQAAICedHcPdAVtRUcFAAAA0BiCCgAAAKAxBBUAAABAY5hRAQAAAD0xo6KldFQAAAAAjSGoAAAAABpDUAEAAAA0hhkV/yCe/81PZ6MD98riufNz9Ts/kZk33PqMNfv++sQMH79huubNT5Jc9sp3Z8GMR7P1h96ZLd7zxnQv7sqCGY/m6nd/KnPve7DVp0AbuuJPU/OlE29Id3fNG172nBz+2q1XOL5wUVc+/t1rc8vdM7PuiKE59t92z4QN1s7v/zwtXz/5pizq6s7gzo587NAds/vzNkySnH/V/fnembelu7tm713G5yNv3WEgTg2SJJf/7rZ86atnpru7O298/e45/LB9Vzj+oxN/k1NPvyadnR0ZM3pEjj7qzdl4ozEDVC303g/++dN59fZ7ZPrsmdn+i4cOdDmwgiuuuy9fOu7KJT9fHLB1Dn/LziscX7iwKx//2mW55c6Hs+6oYTn20y/PhHEjs2hxVz5z7OW59c6H09XVnYNesWX+5a1LHnvi6X/OqRfcllqTNx64dd7xej9f8DTddaAraCs6Kv4BbHTAnhk5abOcM+mVufbwz+YF3/1/f3PtlYd+JBfsfHAu2PngLJjxaJLk0Rtuy4W7HpILdnxt7jvtouz8tY+2qHLaWVd3zVE/+mNO+NhLc+4x++e8K+/L5CmPr7DmtN/cnVFrD8nF3zgw7zhgUr5+8k1JktEjh+S7H31JzvnqfvnK+3fLx467Jkkyc/aCHHPSn/LjT++Vc4/ZLzMem5+rbp7W8nODJOnq6s5RR5+e73/38Jx35sdz7gV/zOS/Tl1hzTZbb5xfnvyhnPPLj2a/V+yQY75x7gBVC33z46vOy/7f/tBAlwHP0NXVnaO+/fuccPSBOff7b8p5v56cyffOXGHNaRfenlEjhubin7w173j99vn6969Oklx4+V1ZtKgr55zwxvzyuNfn/867NVOmzs5f7n40p15wW0759uty5v++Ib+5+r7c+8CsgTg9YClBxT+AjQ/aN3efeGaS5JFr/pQh647KsHEb9Prx039zzbIui0euvjFrTRjXH2XCCm6a/Gg2GTsiE8eOyJBBHTnwRRNz6R8eWGHNpdc/mINfulmSZL8XTshVN09PrTXbbjY6Y0cPT5JMmjAqCxZ2ZeGirkyZPiebjhuZMaOGJklevN3YXHztis8JrXLTzfdl003Wz8QJ62XI4EF51f4759Jf37zCmt13m5Thw4ckSXbaYdNMnfbYAFQKfXfF5Bvz6JzHn30htNhNd0zPJhuNysTxozJkcGcO3Pu5ufTKe1ZYc+mV9+TgV26ZJNlvz+fkqhseTK01JSVz5y/K4q7uzF/YlcGDOjNircG5676Z2WHrDTN82OAM6uzIC3YYn1/97u4BODvgSYKKfwBrbTw2c+9/6lO6uVOmZq2Nx6507e4/OjoH3HBmtvvMESs9vsVhb8iDF1zeL3XC8qbNnJfx6621bHvcmLUy7dF5K6yZPnNexq+3JJAY1NmRkWsNzmOzF66w5qJrH8i2m43OkMGd2WTsiNz90OxMmTEni7u6c8n1D+ShR+b2/8nASkybNivjxq67bHvs2HUzbfrf/gTutDOuyZ4v2aYFlQGsuaY9PDfjNxixbHvc+mtn2sNzVlgz/ZE5y9YM6uzIyLWH5LHH52e/PTfPWsMG56Vv/mn2OfTnefcbd8i6o4Zl0mZjcv2fp2bm4/Mzb/6i/Pba+/LQjCdael7Aino9o6KUskGS9ybZbPnH1VrfvfrL4u9x5aEfybwHp2fQiLXz0l9+K5v/80G5+6dnLTu+2aGvzZhdt8sle71tAKuE3rtzyqx8/eSb8oNP7pkkWWfEkHz+XbvkyG9dnVKSnbdcP/dP84MEzXfWudfn5lvuz89+9IGBLgWgbf359hnp6Ci5/Bdvy+OzF+bQI8/Ki3eZkC02HZ33vnmnHPaJ87LWsEHZZov109lRBrpcmqa7e6AraCt9GaZ5VpIrklySpOvZFpdSDk9yeJIclg2zT9b9e+prW5OO+Kc8971vSpI8ct2fs9bEpy7XWGvCuMx94JnX5c97cHqSZPETc3LPSedmvd12WBZUjN33RXnep9+XS/Z6W7oXLmrBGdDuxo4evkK3w9RH52bsmOErrNlw9PA89Mi8jFtvrSzu6s7suYuy7sglbfJTH5mbDxx7Zb76/t2yydinPjnZ5/kbZZ/nb5Qk+b9L7/KDBANm7Nh1VriUY9q0xzJ2w3Wese7Kq/+S751wSX72w3/NkCFmWAOsirHrr7VCt8PUh+dk7Pprr7Bmw/XWzkMznsi4DUYs+flizsKsO2pYzr3s+rx014kZPKgz640enl2eNy43/2VGJo4flTccsHXecMCSod/H/uCajFuuawNovb5c+rFWrfXjtdZTaq2/fPLrby2utR5fa9211rqrkKLv7jzupGVDMaeceUk2f/vBSZL1XrhjFs2anflTZ6ywvnR2Zuh6o5d8P2hQNn713nns5juTJKN32ia7/e9Rufy17182YBP62/ZbjM69U5/IlOlzsnBxd86/6v5lAcOT9nn+RjnzinuSJBddMyW7P2/DlFLy+JyF+ZdjfpcPv2X77LLV+is85pFZS+atzHpiYU6+ZHLe8LLNW3I+8HTbP29i7rl3Ru6f8kgWLlqc8y68Ifvsvd0Ka269bUo+d9Sp+e63Dst6640coEoB1hzbb7Vh7n1gVqY89HgWLurK+b+ZnH1etOkKa/Z50aY58+K/JEkuuvyu7L7TRimlZPyGI3P1jUtmW82dtyh/um1anjNx3STJIzOXXJ764PTZ+dXv78mr93lu604KeIa+fLRzbinlwFrr+f1WDSv14Pm/zUYH7pXXTP5VuubOy9Xv+tSyYwfccGYu2PngdAwdkpdd9P2UwYNTOjsy7ZKr8tcTTkmS7HzMxzJoxFp5yanfTJLMue+hXH7Q+wfkXGgfgzo78tl37pzDvnJ5urtrDtl780yasE6+derN2e45Y7LP8zfKG/bePB877tq88kPnZ521h+TYD+6eJPn5xZNz37QnctwZt+a4M5bcivcHn9gz660zLF868cbccd9jSZIjXrdtNh/vlz8GxqBBnfncp16f97z/+HR1deeQg3fLpOeOyze/c0G223Zi9n3Zdvnasedk7twF+feP/CRJMn7c6Hzv24cNcOXw7E5691HZe8tdsv6IdXP/0Wfn8+eekB9eec5AlwVLfr74wEty2CfPX/LzxX5bZdJmY/KtH1+X7bbcIPu8eLO84YCt87Gv/DqvfMfJWWfk0Bz76ZcnSf7poOflU8f8Jq9+zympteb1+22VrZ6zXpLk3466OI89Pj+DBnXkcx/YI6NGDB3I04S2V2rt3f1gSymzk6ydZOHSr5Kk1lpHPdtjTypbueks//Deev0bB7oEWC3Kdi8a6BJglZX/+OJAlwCrRfcn3zTQJcBqUTY5co2+Hrf79Hetkb/Tdrz+R438e+t1R0Wt1ceWAAAAtJ3atUbmFI3V6xkVZYm3lVI+u3R7Yillt/4rDQAAAGg3fRmmeVySFyX5p6XbTyT5zmqvCAAAAGhbfRmm+cJa6y6llBuSpNY6s5QypJ/qAgAAANpQX4KKRaWUziQ1SUopGyTp7peqAAAAoCm6zahopb5c+vGtJGck2bCU8qUkv0tydL9UBQAAALSlvtz14+ellD8k2TdLbk16cK31tn6rDAAAAGg7vQ4qSinfSvKLWqsBmgAAAEC/6MuMij8k+UwpZassuQTkF7XW6/unLAAAAGiILjMqWqnXMypqrT+ptR6Y5AVJ7kjy1VLKnf1WGQAAANB2+jJM80nPTbJ1kk2T3L56ywEAAADaWa+DilLK15Z2UByV5OYku9ZaX9NvlQEAAABtpy8zKv6a5EW11of7qxgAAABomtptRkUrPWtQUUrZutZ6e5LrkmxSStlk+eO11j/2V3EAAABAe+lNR8WRSQ5P8vWVHKtJ9lmtFQEAAABt61mDilrr4aWUjiSfqbX+vgU1AQAAAG2qV8M0a63dSf6nn2sBAAAA2lxfhmleWko5JMnptVaTRAAAAGgPXX4FbqVe3540yb8kOTXJwlLK46WU2aWUx/upLgAAAKAN9bqjotY6sj8LAQAAAOhVUFFKGZTkgCRbL911a5KLaq2L+6swAAAAoP08a1BRStk4yWVJHkpyQ5KS5NVJji2lvKzW+mD/lggAAAADqKt7oCtoK73pqPhSku/WWv97+Z2llH9L8uUk7+iHugAAAIA21JugYvda6zufvrPW+q1Syh2rvyQAAACgXfXmrh/zejg2d3UVAgAAANCbjop1SimvX8n+kmTUaq4HAAAAGqV214Euoa30Jqj4bZLX/I1jl6/GWgAAAIA296xBRa31Xb15olLKO2qtP1n1kgAAAIB21ZsZFb3176vxuQAAAIA21JtLP3qrrMbnAgAAgGboMqOilVZnR4W/OQAAAGCVrM6gQkcFAAAAsEpWZ1Dx+9X4XAAAAEAb6nVQUUr591LKqLLED0opfyylvPLJ47XWD/RPiQAAAEC76MswzXfXWr9ZStkvyegk/5zkp0ku7pfKAAAAoAm6jWRspb5c+vHkDIoDk/y01npLzKUAAAAAVqO+BBV/KKVcnCVBxUWllJFJuvunLAAAAKAd9eXSj8OS7JTkrlrr3FLKekne1S9VAQAAAG2p10FFrbW7lLI4yZ6llOUfd9PqLwsAAACaoXaZUdFKvQ4qSik/TLJDklvy1CUfNcnp/VAXAAAA0Ib6cunH7rXWbfutEgAAAKDt9WWY5lWlFEEFAAAA0G/60lFxYpaEFVOTLMiSW5PWWusO/VIZAAAANEG3G162Ul+Cih8k+eckf47bkgIAAAD9oC9BxYxa69n9VgkAAADQ9voSVNxQSjkpyTlZculHkqTW6q4fAAAAwGrRl6BieJYEFK9cbp/bkwIAALBm66oDXUFbedagopQysdZ6f631XSs59ur+KQsAAABoR725PemvSimbPX1nKeVdSb652isCAAAA2lZvgoojk1xcSpn05I5SyieX7t+rvwoDAAAA2s+zXvpRaz2/lLIgyQWllIOTvCfJbkn2rLXO7Of6AAAAgDbSq2GatdZLl17q8ZskVybZp9Y6vz8LAwAAgCao3YZptlJvhmnOzpK7e5QkQ5Psm2R6KaUkqbXWUf1bIgAAANAuenPpx8hWFAIAAADQm2GaAAAAAC3RqxkVAAAA0La6zKhoJR0VAAAAQGMIKgAAAIDGEFQAAAAAjWFGBQAAAPTEjIqW0lEBAAAANIagAgAAAGgMQQUAAADQGGZUAAAAQA9qtxkVraSjAgAAAGgMQQUAAADQGIIKAAAAoDEEFQAAAEBjGKYJAAAAPenqHugK2oqOCgAAAKAxBBUAAABAYwgqAAAAgMYwowIAAAB6ULvrQJfQVnRUAAAAAI0hqAAAAAAaQ1ABAAAANIYZFQAAANCTLjMqWklHBQAAANAYggoAAACgMQQVAAAAQGOYUQEAAAA96TajopV0VAAAAACNIagAAAAAGkNQAQAAADSGoAIAAABoDMM0AQAAoAe1yzDNVtJRAQAAADSGoAIAAADok1LKmFLKr0opdy79c/RK1uxUSrmqlHJLKeWmUsqbe/PcggoAAACgrz6R5NJa66Qkly7dfrq5Sd5ea31ekv2T/HcpZd1ne2IzKgAAAKAn3WZUrMRBSfZe+v1PkvwmyceXX1Br/cty3z9YSpmeZIMkj/X0xDoqAAAAgL4aW2t9aOn3U5OM7WlxKWW3JEOS/PXZnlhHBQAAALShUsrhSQ5fbtfxtdbjlzt+SZJxK3nop5ffqLXWUsrfbDsppYxP8tMk76i1dj9bXYIKAAAAaENLQ4njezj+8r91rJQyrZQyvtb60NIgYvrfWDcqyXlJPl1rvbo3dQkqAAAAoCddz9oE0I7OTvKOJF9Z+udZT19QShmS5IwkJ9ZaT+vtE5tRAQAAAPTVV5K8opRyZ5KXL91OKWXXUsr3l655U5I9k7yzlHLj0q+dnu2JdVQAAAAAfVJrfSTJvivZf32S9yz9/mdJftbX59ZRAQAAADSGjgoAAADoQe3+mze0oB/oqAAAAAAaQ1ABAAAANIagAgAAAGgMQQUAAADQGIZpAgAAQE+6DNNsJR0VAAAAQGO0pKPidZ95biteBvpV9x33DXQJsFqURYsGugRYZd2ffNNAlwCrRceXTxnoEmC1qN89cqBLYA2iowIAAABoDDMqAAAAoAe124yKVtJRAQAAADSGoAIAAABoDEEFAAAA0BhmVAAAAEAPapcZFa2kowIAAABoDEEFAAAA0BiCCgAAAKAxzKgAAACAHtRuMypaSUcFAAAA0BiCCgAAAKAxBBUAAABAYwgqAAAAgMYwTBMAAAB60N1lmGYr6agAAAAAGkNQAQAAADSGoAIAAABoDDMqAAAAoAe124yKVtJRAQAAADSGoAIAAABoDEEFAAAA0BhmVAAAAEAPanf3QJfQVnRUAAAAAI0hqAAAAAAaQ1ABAAAANIYZFQAAANCD2lUHuoS2oqMCAAAAaAxBBQAAANAYggoAAACgMQQVAAAAQGMYpgkAAAA9qN2GabaSjgoAAACgMQQVAAAAQGMIKgAAAIDGMKMCAAAAelC7zKhoJR0VAAAAQGMIKgAAAIDGEFQAAAAAjWFGBQAAAPSgdptR0Uo6KgAAAIDGEFQAAAAAjSGoAAAAABrDjAoAAADoQbcZFS2lowIAAABoDEEFAAAA0BiCCgAAAKAxBBUAAABAYximCQAAAD2oXYZptpKOCgAAAKAxBBUAAABAYwgqAAAAgMYwowIAAAB6ULvNqGglHRUAAABAYwgqAAAAgMYQVAAAAACNYUYFAAAA9MCMitbSUQEAAAA0hqACAAAAaAxBBQAAANAYZlQAAABAD2qXGRWtpKMCAAAAaAxBBQAAANAYggoAAACgMQQVAAAAQGMYpgkAAAA9qN3dA11CW9FRAQAAADSGoAIAAABoDEEFAAAA0BhmVAAAAEAPalcd6BLaio4KAAAAoDEEFQAAAEBjCCoAAACAxjCjAgAAAHpQu82oaCUdFQAAAEBjCCoAAACAxhBUAAAAAI1hRgUAAAD0oNuMipbSUQEAAAA0hqACAAAAaAxBBQAAANAYZlQAAABAD2qXGRWtpKMCAAAAaAxBBQAAANAYggoAAACgMQQVAAAAQGMYpgkAAAA9qN2GabaSjgoAAACgMQQVAAAAQGMIKgAAAIDGMKMCAAAAelC7zKhoJR0VAAAAQGMIKgAAAIDGEFQAAAAAjWFGBQAAAPSgdptR0Uo6KgAAAIDGEFQAAAAAjSGoAAAAABrDjAoAAADogRkVraWjAgAAAGgMQQUAAADQGIIKAAAAoDEEFQAAAEBjGKYJAAAAPahdhmm2kqDiH8TgA/8lHVvumixakIWnfyP1ob8+Y82gl789nTvtkzJsROb/5xuW7S/rbJDBrz8yZfjaSenIoot/nO47r29l+bSpWmuOvvDeXH7nYxk+uCNHH7xFth2/9jPW3fLgnHzqrL9m/qLu7Dlp3Xxq/01TSsltU+fkC+fenQWLawZ1lHz2VZtlh41HZPb8xfn4GX/NQ7MWZnF3zbteND6v33mDAThD1mRX3DQtR//8z+nurnnDXpvmva/ecoXjCxd15ePH/zG33vNY1h0xJMcesWs23mDJv+/jz/lLfnn5venoKPn027bPS7YfmyT58YWTc9pv700pyZYTRuXo9+ySoUM68/Nf3ZUTL/5r7ps+J1f+zwEZPXJoy8+X9nDFdfflS8ddueTf9QFb5/C37LzC8YULu/Lxr12WW+58OOuOGpZjP/3yTBg3MosWd+Uzx16eW+98OF1d3TnoFVvmX9665LEnnv7nnHrBbak1eeOBW+cdr99hIE4NVuoH//zpvHr7PTJ99sxs/8VDB7ocoJdc+vEPoGPSrinrbZQF//3eLDzr2xnymn9d6bqu26/Jgu996Bn7B+31lnTdfEUWHPdvWXjKVzP4NUf0d8mQJLl88qzc++j8XPjBHfOF12yeL5x390rXHXXe3TnqNZvnwg/umHsfnZ8rJs9Kknz9V/fliL0m5Iz3bZ8PvGxCvv6r+5IkJ103LVusPzxnvG/7/OQd2+RrF9+bhV3dLTsv1nxd3TVfPPFPOf7DL8o5X9435109JZMfeHyFNaddfm/WWXtwLjrmFXn7flvkv065NUky+YHHc/41U3LO0fvkhI+8KEf95E/p6q6Z9ui8/OxXd+W0L+ydc47eN93dNedfMyVJsvOWY/LDj704G60/vNWnShvp6urOUd/+fU44+sCc+/035bxfT87ke2eusOa0C2/PqBFDc/FP3pp3vH77fP37VydJLrz8rixa1JVzTnhjfnnc6/N/592aKVNn5y93P5pTL7gtp3z7dTnzf9+Q31x9X+59YNZAnB6s1I+vOi/7f/uZPx8DzdaroKKU0llK8V/4AOncZvd03XhZkqROuSMZvnYyYvQz1tUpdyRPzHzG/qSmDFsrSVKGrZ06+9H+LBeWuez2mTloh/VTSsmOE0Zm9vyuzJi9cIU1M2YvzBMLurLjhJEppeSgHdbPpbcv+XdcSsmcBV1JkifmL86GI4cs2Z9kzsKu1Fozd2FX1hk+KIM6SkvPjTXbTXfNzCZjR2TihmtnyKCOHPjCCbnsj1NXWHPZH6fmoJdskiTZ7wUb5epbZ6TWmsv+ODUHvnBChgzuzIQN1s4mY0fkpruW/Jvu6q6Zv7Ari7u6M29hVzZcd0kwse2m6y7rxoD+ctMd07PJRqMycfyoDBncmQP3fm4uvfKeFdZceuU9OfiVS7qH9tvzObnqhgdTa01Jydz5i7K4qzvzF3Zl8KDOjFhrcO66b2Z22HrDDB82OIM6O/KCHcbnV79beSgNA+GKyTfm0TmPP/tCoFF6delHrbWrlPLWJN/o53pYiTJqvdRZM5Zt11kPL9m30lDimRZd9vMMfed/ZtALX5MMGZYFP/50f5UKK5g+e2HGrfNUC/vYUUMybfbCbLA0cEiSabMXZuyoISusmb40zPjEfpvmvT+7Pcf86r5015qfv/t5SZJDdxuXf/3FHdnr2BsyZ0FXjn3Dc9NRBBWsPtNnzsu4MU91N4wdMyw3/XXF/+dOmzkv45euGdTZkZHDB+WxJxZm2sx52XGLMSs8dvrMedn5uWPyrgOem32PvChDh3Rmj+02zB7bb9iaE4Ik0x6em/EbjFi2PW79tfOn26evsGb6I3OWrRnU2ZGRaw/JY4/Pz357bp7LrronL33zTzN/weJ84n0vyrqjhmXSZmPyjR9dl5mPz8+wIZ357f9v797jtSqrRY//BldRQFEQUQnv4gVEIJPc3sg0y6OZWnunxzxqZnasY6dO5q0yM/fHrJ2mlZZa7t2u3FvFyjaaiqiJKIJXTMUrXhC8cdnIbY3zx5zIKy0W74J1mWut3/fzWZ8117Pm5XnhWe8755jjGXPqi+y+k1PxJHU+DQ3WqGhLzalRcW9E/AT4HbBoZWNmPtTYyhFxCnAKwGUf352TRn9gffqp9dBj5P6seOgvLP/rjXQbOpxeR/1flvzkNEj/2FRtv31wDmceMoyDd92UPz/+Bufe/CxXH78L98x6m+GDN+Ka43fhxbeWcPJ1TzJmWD/69rbsjqrrnUVLueOhV7ntBwfTb8OenHH5VG6+9yUO32doe3dNWqtHn5xLt27B5N8ex/wFSzn2qxP48Oit2X7YAD7/mVGcdOaf2HCDHuyy/UC6m+EmSVpPzTmrH1V+P7+mLYHxja2cmVcCVwIsPvcTXhE3U/e9PkGPsR8DoOHlp4iNV92diI0HkvPfqH9fYw5m6a/OK/b10pPQoxds2B8WOYdULe83U1/j+oeKDKARW27Ea+8sAfoBMGf+UgbXZFMADO7XiznzV00HmTN/6XtTPCY8PI+zPjYMgI/tuinn3fwsADfOmMfJ+wwhIhi26QZsvUlvnp33LiO36ovUEjYf0IfX3lz83s9z3nyXwQPeXz9i8IA+vPpmkXmxfEUDCxYvZ5O+vRjcyLabD+jDfY/PZatBG7Jp/yLL6KAxWzL9mTcNVKjNDB64Ia/OXfjez6/NW8Tgge+fcrT5Zhvx6tyFbDGobzGuFy1lk/4b8Mc7HmTfsUPp2aM7mw3ow+jdtuCxp+YydEh/jj50OEcfOhyAH/7yfrYY5HuxJGn91F1MMzMPbOSr0SCF1t+KqX9iyRWns+SK01kxcwrdRxX/1LH1zvDuojXUomhcvj2XbtuPKrYfNJTo0dMghVrNZ/faghtPHcGNp47gI8MHMOGReWQmD89eQL/e3d837QNgUL9e9O3dnYdnLyAzmfDIPMYPL2qwbN6vJw+8sACAKc/NZ9hmGwAwpH8vpjxXzDedt3AZz72xmKEDfEqCWs6IbTfhhTkLmT13EUuXN3DL/bM5cM8t3rfOgXtuwYR7igKvEx94hb13KeqxHLjnFtxy/2yWLlvB7LmLeGHOQkZuN4Ahm/Xh4WfeYvGS5WQmU56Yy/ZbekGntjNi58154eV3mP3qfJYuW8Etk55h/Lhh71tn/Lhh3HTrUwBMnPwse4/akohgyOb9mDLjZQD+e/EyHp45h+2GbgLAG28VgblXXl/Abfc+z2Hjd2i7FyVJ6pQi60z/j4jBwIXAlpl5aETsCozLzF+ubVszKtZfz8O+SLcdx6x6POkrzwDQ+7TLWHLF6QD0OPh/0WPkAdBvU1jwJsunTWT5nb8hBg2l5xFfJnpvAAnLJl5Nw6zp7fhqOqZeu2zW3l3ocDKTC255nntmvcMGPbvxvSO2Y/fywuzInz3KjaeOAOCxVxZy1k3PsmR5A/vusAlnH1o8nnTaiwv4/n89z4oG6NUjOO/j27Lblhvx+oKlnHXTLOYuXEYmnPwPW3L4yIHt+VI7lNhuSHt3oUO46+HX+H75eNJP7TeMUw/fmUtvmMnu22zC+NFDWLJ0Bd+4chozX3iHjTfqySWnfZChmxd3p39289+4YfILdO/ejW9+dgT77VE8nvSyG2by56kv071bsMuwjbngxD3p1bM71906i1/e8jTz3lnCpv17s9/IwVxw0p5Nda/Liy0Ht3cXOqS77n+RC39aPJ70qEN25tRjR3PptQ+w+06DGP/hbViydDn/76I7mTlrHhv3680Pzz6IoUP6s2jxMs66eBKzXnyLzORTh+zMSZ8eBcCxZ0zg7fnv0qNHN878wjjGjd66fV9kB9Pt+79v7y50ar858XwO2Gk0A/tuwpz5b/KtP17F1X/9Q3t3q1PKn07p1PO+Hh85vFNe0+72yJOV/H9rTqDiz8A1wNmZuUdE9ACmZ+aItW1roEKdgYEKdRYGKtQZGKhQZ2GgQp2FgYqOqaqBirqnfgADM/P3QANAZi4HVrRKryRJkiRJUpfUnEDFoojYjKKAJhGxN2ChA0mSJEmS1GKa89SPrwI3A9tHxL3AIODoVumVJEmSJEkV0dDQ3j3oWuoOVGTmQxGxP7AzEMDfMnNZq/VMkiRJkiR1Oc3JqADYC9im3G50RJCZv27xXkmSJEmSpC6p7kBFRFwHbA/MYFURzQQMVEiSJEmSpBbRnIyKscCuWe/zTCVJkiRJkpqpOYGKx4AtgFdbqS+SJEmSJFWOxTTbVnMCFQOBJyJiKrBkZWNmHt7ivZIkSZIkSV1ScwIV326tTkiSJEmSJEHzAhU7AJMz8+nW6owkSZIkSeramhOo+ADw84jYBpgGTAbuzswZrdAvSZIkSZIqocFHSrSpbvWumJnfyszxwG7A3cDXKQIWkiRJkiSpC4mITSPitoh4uvw+oIl1+0fE7Ij4ST37rjtQERHnRMSfgVsppoF8Ddi63u0lSZIkSVKncSZwe2buCNxe/rwm36WYlVGXugMVwKeAzYC/ADcAEzLTR5VKkiRJktT1HAH8qlz+FfDJxlaKiDHAYIqkh7rUXaMiM0dHRH9gH+CjwJUR8Xpm/kO9+5AkSZIkqaNpaGjvHrSOiDgFOKWm6crMvLLOzQfXJC+8RhGMWH3/3YBLgOOAg+rtV92BiojYHdgX2B8YC7xEUatCkiRJkiR1MGVQYo2BiYj4C7BFI786e7X9ZEQ0VnL0NOCWzJwdEXX3qzlP/fgxcCdwOTA9Mxc2Y1tJkiRJktSBZOYasyAiYk5EDMnMVyNiCPB6I6uNA/aNiNOAvkCviFiYmU3Vs1h7oCIiegAXAnsAAyhqVQyNiGuAszNz2dr2IUmSJEmSOpWbgc8BF5XfJ6y+QmYeu3I5Ik4Axq4tSAH1ZVRcDPQDts3MBeUB+gM/KL++Usc+JEmSJEnqkDprjYr1dBHw+4g4CXgB+DRARIwFTs3Mk9d1x/UEKg4DdsrM9+abZOb8iPgi8CQGKiRJkiRJ6lIy8w3gI420Pwj8XZAiM68Frq1n3/U8njRrgxQ1jSuAxoplSJIkSZIkrZN6AhVPRMTxqzdGxHEUGRWSJEmSJEktop6pH18CboiIE4FpZdtYoA9wZGt1TJIkSZIkdT1rDVRk5svAhyJiPLBb2XxLZt7eqj2TJEmSJKkCLKbZturJqAAgM+8A7mjFvkiSJEmSpC6unhoVkiRJkiRJbcJAhSRJkiRJqoy6p35IkiRJktQVWaOibZlRIUmSJEmSKsNAhSRJkiRJqgwDFZIkSZIkqTKsUSFJkiRJUhOsUdG2zKiQJEmSJEmVYaBCkiRJkiRVhoEKSZIkSZJUGdaokCRJkiSpCdaoaFtmVEiSJEmSpMowUCFJkiRJkirDQIUkSZIkSaoMAxWSJEmSJKkyLKYpSZIkSVITLKbZtsyokCRJkiRJlWGgQpIkSZIkVYaBCkmSJEmSVBnWqJAkSZIkqQnWqGhbZlRIkiRJkqTKMFAhSZIkSZIqw0CFJEmSJEmqDGtUSJIkSZLUhMxs7y50KWZUSJIkSZKkyjBQIUmSJEmSKsNAhSRJkiRJqgxrVEiSJEmS1ISGhvbuQddiRoUkSZIkSaoMAxWSJEmSJKkyDFRIkiRJkqTKMFAhSZIkSZIqw2KakiRJkiQ1wWKabcuMCkmSJEmSVBkGKiRJkiRJUmUYqJAkSZIkSZVhjQpJkiRJkppgjYq2ZUaFJEmSJEmqDAMVkiRJkiSpMgxUSJIkSZKkyrBGhSRJkiRJTbBGRdsyo0KSJEmSJFWGgQpJkiRJklQZBiokSZIkSVJlWKNCkiRJkqQmWKOibZlRIUmSJEmSKsNAhSRJkiRJqgwDFZIkSZIkqTIMVEiSJEmSpMqwmKYkSZIkSU2wmGbbMqNCkiRJkiRVhoEKSZIkSZJUGQYqJEmSJElSZVijQpIkSZKkJlijom2ZUSFJkiRJkirDQIUkSZIkSaoMAxWSJEmSJKkyrFEhSZIkSVITGrK9e9C1mFEhSZIkSZIqw0CFJEmSJEmqDAMVkiRJkiSpMqxRIUmSJElSExoa2rsHXYsZFZIkSZIkqTIMVEiSJEmSpMowUCFJkiRJkirDQIUkSZIkSaoMi2lKkiRJktQEi2m2LTMqJEmSJElSZRiokCRJkiRJlWGgQpIkSZIkVYY1KiRJkiRJaoI1KtqWGRWSJEmSJKkyDFRIkiRJkqTKMFAhSZIkSZIqwxoVkiRJkiQ1wRoVbcuMCkmSJEmSVBkGKiRJkiRJUmUYqJAkSZIkSZURmdnefVALiIhTMvPK9u6HtL4cy+osHMvqDBzH6iwcy1LHYkZF53FKe3dAaiGOZXUWjmV1Bo5jdRaOZakDMVAhSZIkSZIqw0CFJEmSJEmqDAMVnYdz7tRZOJbVWTiW1Rk4jtVZOJalDsRimpIkSZIkqTLMqJAkSZIkSZVhoKLionBPRBxa03ZMRPxXe/ZLkiRJaksRsXVETIiIpyNiVkT8OCJ6tXe/JLU8AxUVl8XcnFOBH0bEBhHRF7gQ+NK67C8ierRk/9R5RcTZEfF4RDwSETMi4kNNrHttRBxdLk+KiLHl8i0RsUkL9umAiHin7M/MiPjWGtYbGxGXttRx1fFExIpynDwWEddHxIbt0IcDIuLDa1nn2xHxck1fD1/DeqdGxPGt01N1FBGxsGb54xHxVEQMa4XjXBsRz0XEw+Uxfh0RWzex/i8iYteW7odUKyICuAG4KTN3BHYC+gLfa4Nje/4stTEDFR1AZj4G/AH4BnAe8K/A2RExNSKmR8QRABGxTUTcHREPlV8fLtsPKNtvBp5or9ehjiMixgGHAaMzcyRwEPBSc/eTmR/PzLdbuHt3Z+YoYCxwXESMrv1lRPTIzAcz88stfFx1LIszc1Rm7g4spQj4vqeNTjoPAJoMVJR+VI7pY4CrI+J9n83lmP5ZZv665buojigiPgJcChyamS+00mG+npl7ADsD04E7GrtzHRHdM/PkzPT8Qq1tPPBuZl4DkJkrgDOAEyPizogYCVCeG59XLp8fEZ8vz4UnRcR/RMSTEfFvZeCDiBgTEXdFxLSImBgRQ8r2SRHxLxHxIPCV9njBUldmoKLj+A7wWeBQYAPgjszcCzgQuDgiNgJeBz6amaOBz1CcxKw0GvhKZu7Utt1WBzUEmJeZSwAyc15mvrKmD/M1iYjnI2JgGUSbGRFXlVkat0ZEn3KdD9ZkbVwcEY/V08HMXARMA3Yo70pfFxH3AteVJyR/LPffNyKuiYhHy+McVbYfHBH3lUG968tsJXVOd1OMk/cFbSOieznmHijHxhcAImJIREyuyXLYt2xvdMyU4/w7ZfujETE8IrahCI6cUe5n37V1MjNnAsuBgaufIJdj/Gvl8XaIiL+Ud7sfiojty/av17yW77T8P6OqICL2A64CDsvMWWXbtRHx04iYEhHPlmP96vJ999pyne7leo+V4/SMeo6XhR8Br1GcgxARCyPikoh4GBhXjtexUWT+XFzT1xMi4ifl8nFR3GCZERE/j4juNfv6Xjmep0TE4Jb711InsxvF5/57MnM+8CJwJ7BvRGxM8T66T7nKvsDkcnlP4P8AuwLbAftERE/gMuDozBwDXM37MzR6ZebYzLykVV6RpDUyUNFBlBdlvwOuAz4KnBkRM4BJFIGLDwA9gasi4lHgeoo34pWmZuZzbdlndWi3AkOjSPm9IiL2r+PDfG12BC7PzN2At4GjyvZrgC+Ud5RX1LuziNgM2Bt4vGzaFTgoM/9ptVXPBd7JzBFldsgdETEQOKdcfzTwIPDVZrwWdRBRZE4cCjxaNtUGbU+iGBsfBD4IfD4itqUICk8sx+QewIw6xsy8sv2nwNcy83ngZ5TZEpl5dx19/RDQAMwtm9Z0gvxvFH9Le1BkbLwaEQdT/I3tBYwCxpQXtOpcegM3AZ/MzCdX+90AYBzFHeabgR9RXNiNiIhRFONiq8zcPTNHULz3NsdDwPByeSPg/szcIzPvqVnnP4Eja37+DPDbiNilXN6n5r3+2Jp9TSnH82Tg883slwRwF7AfRYDiT0DfKKb8bZuZfyvXmZqZszOzAZgBbEORMbQ7cFt5Xn0OUDvN6Xdt0ntJf8f5Vh1LQ/kVwFE1b7xAMdcZmENxYt0NeLfm14vaqI/qBDJzYUSMobgTcSDFB/UFrPowB+gOvNqM3T6XmTPK5WnANlHUr+iXmfeV7b+hmHLSlH0jYjrF38JFmfl4RBwD3JyZixtZ/yDgH2te21sRcRhFYOPe8rX0Au5rZFt1XH3Kk04oMip+SXFRXxu0PRgYGWV9FWBjiov9ByimYPSkmAs9IyL2p+kxc0P5fRrwqWb29YyIOA5YAHwmM7M8xt+dIEdEP4qLzRsBMvPdsv3g8vVML1ftW76WyavvQx3aMuCvFEG21VPR/1COnUeBOZn5KEBEPE5xQXYXsF1EXEZxIXdrM48dNcsrKIIS75OZc8uMjr2BpykCG/dS1NUaAzxQju0+FFmgUEzN+mO5PI3iZozUmCeAo2sbIqI/xc266RRTQp8FbgMGUgS9ajMwltQsr6C4Dgrg8cwct4Zjev4stRMDFR3TROD0iDi9PCnZMzOnU5xkz87Mhoj4HMWFpLROyrmfk4BJ5Ynvl2j6w3xtVj9B6LOO+7k7MxsLZjTnZCKA2xrJvlDnsbi8c/ue8gKpdpwEcHpmTlx94zIb4RPAtRHxQ+Atmh4zK8f3ypPf5vhRZv6gkfbmjunvZ+bPm3lsdSwNwKeB2yPirMy8sOZ3S2rWWbLaNj3KIO0ewCEU05I+DZzYjGPvCdxeLr9bfkY05rflvp8EbizPUwL4VWZ+s5H1l5WFw2Hd/n7UddwOXBQRx2fmr8vpQ5cA12bm/Ih4iaLWz/nAIOAH5VdT/gYMiohxmXlfGaDeKTMfX8t2klqZUz86pu9STPN4pLxT8t2y/Qrgc+Wc0eEYBdY6ioidI2LHmqZRwEzKD/NynZ4Rsdv6HKcstLkgVj1R5B+bWH1d3UbNU3IiYgAwhWJu6g5l20YRYf2Wrmci8MXyxJSI2KkcC8Mo7khfBfyCYrrIuoyZBUC/luxwZi4AZkfEJ8t+9C7TmydSFJRbWTdjq4jYvCWPrWrIzP+mCKIdGxEn1btdOX2pW2b+J0V6++i1bLJyu4iIL1PULqrn0eg3AkcA/0QRtIDiAvPolWMyIjaNVnhaiTq3MqB1JHBMRDwNPEWRPXxWucrdwOtlduXdFFM4mpx2l5lLKbI0/rk8f55BfUWQJbUyo9YdSGZ+u+bHLzTy+6eBkTVN3yjbJ1HcGZfq1Re4rJyasRx4BjgFuBK4tCxW1QP4F1bViFhXJ1HUVmmgSE1+Zz33t7oLgMujKNK5AvhOZt4QEScA/x4Rvcv1zqE46VHX8QuKlPiHyju+c4FPUjyt4+sRsQxYCBxfprSfQPPGzB+A/4jiyUyn11Onok7/E/h5RJxPMRXgmMy8tawDcF+ZObIQOI5V6fXqRDLzzYj4GDA5IuaudYPCVsA1seqpMo1lN9S6OCLOBTakCNQdWF7Ura1vb0XETGDXzJxatj0REecAt5bHX0YRQG6tJ5aok8rMl4D/sYbfnUtRl4rMfIWa6Uqrnwtn5v+uWZ5BUd9i9f0d0CKdlrROYlW2nSS1vYjom5kLy+UzgSGZ6WPAJEmSpC7KjApJ7e0TEfFNivejF4AT2rc7kiRJktqTGRWSKiciDgH+ebXm5zLzyMbWl6ouIs6mKPJW6/rMbM4jfqUWFRGXUzzOsdaPM7O5jy6VJKlFGaiQJEmSJEmV4VM/JEmSJElSZRiokCRJkiRJlWGgQpIkSZIkVYaBCkmSJEmSVBkGKiRJkiRJUmX8f6grIK9pHk1uAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1440x1440 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "#get correlations of each features in dataset\n",
    "corrmat = df.corr()\n",
    "top_corr_features = corrmat.index\n",
    "plt.figure(figsize=(20,20))\n",
    "#plot heat map\n",
    "g=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap=\"RdYlGn\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "commercial-facing",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Selling_Price</th>\n",
       "      <th>Present_Price</th>\n",
       "      <th>Kms_Driven</th>\n",
       "      <th>Owner</th>\n",
       "      <th>Current Year</th>\n",
       "      <th>no_year</th>\n",
       "      <th>Fuel_Type_Diesel</th>\n",
       "      <th>Fuel_Type_Petrol</th>\n",
       "      <th>Seller_Type_Individual</th>\n",
       "      <th>Transmission_Manual</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3.35</td>\n",
       "      <td>5.59</td>\n",
       "      <td>27000</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.75</td>\n",
       "      <td>9.54</td>\n",
       "      <td>43000</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>7.25</td>\n",
       "      <td>9.85</td>\n",
       "      <td>6900</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2.85</td>\n",
       "      <td>4.15</td>\n",
       "      <td>5200</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4.60</td>\n",
       "      <td>6.87</td>\n",
       "      <td>42450</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Selling_Price  Present_Price  Kms_Driven  Owner  Current Year  no_year  \\\n",
       "0           3.35           5.59       27000      0          2020        6   \n",
       "1           4.75           9.54       43000      0          2020        7   \n",
       "2           7.25           9.85        6900      0          2020        3   \n",
       "3           2.85           4.15        5200      0          2020        9   \n",
       "4           4.60           6.87       42450      0          2020        6   \n",
       "\n",
       "   Fuel_Type_Diesel  Fuel_Type_Petrol  Seller_Type_Individual  \\\n",
       "0                 0                 1                       0   \n",
       "1                 1                 0                       0   \n",
       "2                 0                 1                       0   \n",
       "3                 0                 1                       0   \n",
       "4                 1                 0                       0   \n",
       "\n",
       "   Transmission_Manual  \n",
       "0                    1  \n",
       "1                    1  \n",
       "2                    1  \n",
       "3                    1  \n",
       "4                    1  "
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "composite-austria",
   "metadata": {},
   "outputs": [],
   "source": [
    "X=final_dataset.iloc[:,1:]\n",
    "y=final_dataset.iloc[:,0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "democratic-wound",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 3], dtype=int64)"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X['Owner'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "short-minute",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Present_Price</th>\n",
       "      <th>Kms_Driven</th>\n",
       "      <th>Owner</th>\n",
       "      <th>Current Year</th>\n",
       "      <th>no_year</th>\n",
       "      <th>Fuel_Type_Diesel</th>\n",
       "      <th>Fuel_Type_Petrol</th>\n",
       "      <th>Seller_Type_Individual</th>\n",
       "      <th>Transmission_Manual</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5.59</td>\n",
       "      <td>27000</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>9.54</td>\n",
       "      <td>43000</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>9.85</td>\n",
       "      <td>6900</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.15</td>\n",
       "      <td>5200</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>6.87</td>\n",
       "      <td>42450</td>\n",
       "      <td>0</td>\n",
       "      <td>2020</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Present_Price  Kms_Driven  Owner  Current Year  no_year  Fuel_Type_Diesel  \\\n",
       "0           5.59       27000      0          2020        6                 0   \n",
       "1           9.54       43000      0          2020        7                 1   \n",
       "2           9.85        6900      0          2020        3                 0   \n",
       "3           4.15        5200      0          2020        9                 0   \n",
       "4           6.87       42450      0          2020        6                 1   \n",
       "\n",
       "   Fuel_Type_Petrol  Seller_Type_Individual  Transmission_Manual  \n",
       "0                 1                       0                    1  \n",
       "1                 0                       0                    1  \n",
       "2                 1                       0                    1  \n",
       "3                 1                       0                    1  \n",
       "4                 0                       0                    1  "
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "dimensional-sustainability",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    3.35\n",
       "1    4.75\n",
       "2    7.25\n",
       "3    2.85\n",
       "4    4.60\n",
       "Name: Selling_Price, dtype: float64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "leading-closure",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ExtraTreesRegressor()"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "### Feature Importance\n",
    "\n",
    "from sklearn.ensemble import ExtraTreesRegressor\n",
    "import matplotlib.pyplot as plt\n",
    "model = ExtraTreesRegressor()\n",
    "model.fit(X,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "sensitive-submission",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.36971296 0.04014219 0.00169095 0.         0.07850416 0.22862191\n",
      " 0.01152343 0.129414   0.1403904 ]\n"
     ]
    }
   ],
   "source": [
    "print(model.feature_importances_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "flexible-liabilities",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot graph of feature importances for better visualization\n",
    "feat_importances = pd.Series(model.feature_importances_, index=X.columns)\n",
    "feat_importances.nlargest(5).plot(kind='barh')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "resident-width",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "blessed-anxiety",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestRegressor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "normal-virus",
   "metadata": {},
   "outputs": [],
   "source": [
    "regressor=RandomForestRegressor()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "enclosed-notification",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "dried-disco",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]\n"
     ]
    }
   ],
   "source": [
    "n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]\n",
    "print(n_estimators)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "intermediate-string",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import RandomizedSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "french-driver",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Randomized Search CV\n",
    "\n",
    "# Number of trees in random forest\n",
    "n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]\n",
    "# Number of features to consider at every split\n",
    "max_features = ['auto', 'sqrt']\n",
    "# Maximum number of levels in tree\n",
    "max_depth = [int(x) for x in np.linspace(5, 30, num = 6)]\n",
    "# max_depth.append(None)\n",
    "# Minimum number of samples required to split a node\n",
    "min_samples_split = [2, 5, 10, 15, 100]\n",
    "# Minimum number of samples required at each leaf node\n",
    "min_samples_leaf = [1, 2, 5, 10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "organic-freeze",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'n_estimators': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200], 'max_features': ['auto', 'sqrt'], 'max_depth': [5, 10, 15, 20, 25, 30], 'min_samples_split': [2, 5, 10, 15, 100], 'min_samples_leaf': [1, 2, 5, 10]}\n"
     ]
    }
   ],
   "source": [
    "# Create the random grid\n",
    "random_grid = {'n_estimators': n_estimators,\n",
    "               'max_features': max_features,\n",
    "               'max_depth': max_depth,\n",
    "               'min_samples_split': min_samples_split,\n",
    "               'min_samples_leaf': min_samples_leaf}\n",
    "\n",
    "print(random_grid)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "compound-lucas",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the random grid to search for best hyperparameters\n",
    "# First create the base model to tune\n",
    "rf = RandomForestRegressor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "resistant-collector",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Random search of parameters, using 3 fold cross validation, \n",
    "# search across 100 different combinations\n",
    "rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid,scoring='neg_mean_squared_error', n_iter = 10, cv = 5, verbose=2, random_state=42, n_jobs = 1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "hydraulic-summary",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 5 folds for each of 10 candidates, totalling 50 fits\n",
      "[CV] END max_depth=10, max_features=sqrt, min_samples_leaf=5, min_samples_split=5, n_estimators=900; total time=   0.8s\n",
      "[CV] END max_depth=10, max_features=sqrt, min_samples_leaf=5, min_samples_split=5, n_estimators=900; total time=   0.8s\n",
      "[CV] END max_depth=10, max_features=sqrt, min_samples_leaf=5, min_samples_split=5, n_estimators=900; total time=   0.8s\n",
      "[CV] END max_depth=10, max_features=sqrt, min_samples_leaf=5, min_samples_split=5, n_estimators=900; total time=   0.8s\n",
      "[CV] END max_depth=10, max_features=sqrt, min_samples_leaf=5, min_samples_split=5, n_estimators=900; total time=   0.8s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=1100; total time=   1.3s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=1100; total time=   1.0s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=1100; total time=   0.9s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=1100; total time=   1.0s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=1100; total time=   1.0s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=100, n_estimators=300; total time=   0.2s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=100, n_estimators=300; total time=   0.2s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=100, n_estimators=300; total time=   0.2s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=100, n_estimators=300; total time=   0.2s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=100, n_estimators=300; total time=   0.2s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=5, n_estimators=400; total time=   0.4s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=5, n_estimators=400; total time=   0.3s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=5, n_estimators=400; total time=   0.3s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=5, n_estimators=400; total time=   0.3s\n",
      "[CV] END max_depth=15, max_features=auto, min_samples_leaf=5, min_samples_split=5, n_estimators=400; total time=   0.3s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=10, min_samples_split=5, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=10, min_samples_split=5, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=10, min_samples_split=5, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=10, min_samples_split=5, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=10, min_samples_split=5, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=25, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=1000; total time=   1.0s\n",
      "[CV] END max_depth=25, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=1000; total time=   1.0s\n",
      "[CV] END max_depth=25, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=1000; total time=   1.0s\n",
      "[CV] END max_depth=25, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=1000; total time=   1.0s\n",
      "[CV] END max_depth=25, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=1000; total time=   0.9s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=10, min_samples_split=15, n_estimators=1100; total time=   1.0s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=10, min_samples_split=15, n_estimators=1100; total time=   1.0s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=10, min_samples_split=15, n_estimators=1100; total time=   0.9s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=10, min_samples_split=15, n_estimators=1100; total time=   0.9s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=10, min_samples_split=15, n_estimators=1100; total time=   0.9s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=1, min_samples_split=15, n_estimators=300; total time=   0.2s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=1, min_samples_split=15, n_estimators=300; total time=   0.2s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=1, min_samples_split=15, n_estimators=300; total time=   0.2s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=1, min_samples_split=15, n_estimators=300; total time=   0.2s\n",
      "[CV] END max_depth=15, max_features=sqrt, min_samples_leaf=1, min_samples_split=15, n_estimators=300; total time=   0.2s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=700; total time=   0.5s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=5, max_features=sqrt, min_samples_leaf=2, min_samples_split=10, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=1, min_samples_split=15, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=1, min_samples_split=15, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=1, min_samples_split=15, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=1, min_samples_split=15, n_estimators=700; total time=   0.6s\n",
      "[CV] END max_depth=20, max_features=auto, min_samples_leaf=1, min_samples_split=15, n_estimators=700; total time=   0.6s\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "RandomizedSearchCV(cv=5, estimator=RandomForestRegressor(), n_jobs=1,\n",
       "                   param_distributions={'max_depth': [5, 10, 15, 20, 25, 30],\n",
       "                                        'max_features': ['auto', 'sqrt'],\n",
       "                                        'min_samples_leaf': [1, 2, 5, 10],\n",
       "                                        'min_samples_split': [2, 5, 10, 15,\n",
       "                                                              100],\n",
       "                                        'n_estimators': [100, 200, 300, 400,\n",
       "                                                         500, 600, 700, 800,\n",
       "                                                         900, 1000, 1100,\n",
       "                                                         1200]},\n",
       "                   random_state=42, scoring='neg_mean_squared_error',\n",
       "                   verbose=2)"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf_random.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "stock-nebraska",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'n_estimators': 1000,\n",
       " 'min_samples_split': 2,\n",
       " 'min_samples_leaf': 1,\n",
       " 'max_features': 'sqrt',\n",
       " 'max_depth': 25}"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf_random.best_params_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "reduced-china",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-3.671638315307157"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rf_random.best_score_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "determined-router",
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions=rf_random.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "freelance-portal",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\users\\atharva pathak\\anaconda3\\envs\\car\\lib\\site-packages\\seaborn\\distributions.py:2557: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "  warnings.warn(msg, FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Selling_Price', ylabel='Density'>"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.distplot(y_test-predictions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "crude-museum",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x246dc2eb648>"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(y_test,predictions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "cognitive-sandwich",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import metrics\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "plastic-master",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE: 0.8559920879120873\n",
      "MSE: 3.6837650183340664\n",
      "RMSE: 1.9193136841939273\n"
     ]
    }
   ],
   "source": [
    "print('MAE:', metrics.mean_absolute_error(y_test, predictions))\n",
    "print('MSE:', metrics.mean_squared_error(y_test, predictions))\n",
    "print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "honest-anthropology",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "# open a file, where you ant to store the data\n",
    "file = open('random_forest_regression_model.pkl', 'wb')\n",
    "\n",
    "# dump information to that file\n",
    "pickle.dump(rf_random, file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "psychological-hungarian",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
