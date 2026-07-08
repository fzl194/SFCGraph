---
id: UNC@20.15.2@MMLCommand@LST SUFFIXS1TAIAREA
type: MMLCommand
name: LST SUFFIXS1TAIAREA（查询UPF服务区名称以TAC后缀方式绑定的S1TAI范围）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SUFFIXS1TAIAREA
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP跟踪区管理
- TAC后缀绑定UP区域
status: active
---

# LST SUFFIXS1TAIAREA（查询UPF服务区名称以TAC后缀方式绑定的S1TAI范围）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于查询UPF服务区名称以TAC后缀方式绑定的S1TAI范围。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | UPF服务区名称 | 可选必选说明：可选参数<br>参数含义：该参数用于标识UPF服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST UPAREA查询结果中的AREANAME保持一致；且该AREANAME在命令LST UPAREA查询结果中对应的AREATYPE取值应为S1TAI。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SUFFIXS1TAIAREA]] · UPF服务区名称以TAC后缀方式绑定的S1TAI范围（SUFFIXS1TAIAREA）

## 使用实例

- 查询UPF服务区名称为"UPAREA1"的区域以TAC后缀方式绑定的S1TAI。 LST SUFFIXS1TAIAREA: AREANAME="UPAREA1";
  ```
  %%LST SUFFIXS1TAIAREA: AREANAME="UPAREA1";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
           UPF服务区名称  =  uparea1
  	    移动国家码  =  460
  	      移动网号  =  01
  	 TAC范围起始值  =  000
  	 TAC范围结束值  =  111
  		  区号  =  11
  (结果个数 = 1)
  ```
- 查询所有UPF服务区名称以后缀方式绑定的S1TAI。 LST SUFFIXS1TAIAREA:;
  ```
  %%LST SUFFIXS1TAIAREA:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  UPF服务区名称  移动国家码  移动网号  TAC范围起始值  TAC范围结束值  区号
  uparea1        460         01        000            111            11 
  s1area1001     460         03        000            099            09               
  s1area1001     460         03        100            199            09               
  (结果个数 = 3)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UPF服务区名称以TAC后缀方式绑定的S1TAI范围（LST-SUFFIXS1TAIAREA）_23622966.md`
