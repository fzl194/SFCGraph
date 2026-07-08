---
id: UNC@20.15.2@MMLCommand@LST SUFFIXLAIAREA
type: MMLCommand
name: LST SUFFIXLAIAREA（查询UPF服务区名称以LAC后缀方式绑定的LAI范围）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SUFFIXLAIAREA
command_category: 查询类
applicable_nf:
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP跟踪区管理
- LAC后缀绑定UP区域
status: active
---

# LST SUFFIXLAIAREA（查询UPF服务区名称以LAC后缀方式绑定的LAI范围）

## 功能

**适用NF：GGSN**

该命令用于查询UPF服务区名称以LAC后缀方式绑定的LAI范围。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | UPF服务区名称 | 可选必选说明：可选参数<br>参数含义：该参数用于标识UPF服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST UPAREA查询结果中的AREANAME保持一致；且该AREANAME在命令LST UPAREA查询结果中对应的AREATYPE取值应为LAI。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SUFFIXLAIAREA]] · UPF服务区名称以LAC后缀方式绑定的LAI范围（SUFFIXLAIAREA）

## 使用实例

- 查询UPF服务区名称为"iuarea1"的区域以LAC后缀方式绑定的LAI。 LST SUFFIXLAIAREA: AREANAME="iuarea1";
  ```
  %%LST SUFFIXLAIAREA: AREANAME="iuarea1";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
              UPF服务区名称  =  iuarea1
  	       移动国家码  =  460
  		 移动网号  =  01
  	    LAC范围起始值  =  000
  	    LAC范围结束值  =  111
  	             区号  =  11
  (结果个数 = 1)
  ```
- 查询所有UPF服务区名称以LAC后缀方式绑定的LAI。 LST SUFFIXLAIAREA:;
  ```
  %%LST SUFFIXLAIAREA:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  UPF服务区名称  移动国家码  移动网号  LAC范围起始值  LAC范围结束值  区号
  iuarea1        460         01        000            111            11 
  area1001       460         03        000            099            09               
  area1001       460         03        100            199            09               
  (结果个数 = 3)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SUFFIXLAIAREA.md`
