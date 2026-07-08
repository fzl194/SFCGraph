---
id: UNC@20.15.2@MMLCommand@LST UPAREA
type: MMLCommand
name: LST UPAREA（查询UPF服务区）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPAREA
command_category: 查询类
applicable_nf:
- SMF
- GGSN
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
- UP区域管理
status: active
---

# LST UPAREA（查询UPF服务区）

## 功能

**适用NF：SMF、GGSN、SGW-C、PGW-C**

该命令用于查询UPF服务区域。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | UPF服务区名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置UPF服务区的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与LST PNFSMFSERAREA查询结果中的SMFSERVINGAREA保持一致。 |
| AREATYPE | UPF服务区类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置UPF服务区的类型。<br>数据来源：全网规划<br>取值范围：<br>- S1TAI（4G类型的TAI）<br>- N2TAI（5G类型的TAI）<br>- LAI（23G类型的LAI）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UPF服务区（UPAREA）](configobject/UNC/20.15.2/UPAREA.md)

## 使用实例

- 查询区域名称为"UPAREA1"的UPF服务区域信息。 LST UPAREA: AREANAME="UPAREA1";
  ```
  %%LST UPAREA: AREANAME="UPAREA1";%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  UPF服务区名称  =  uparea1
  UPF服务区类型  =  4G TAI
  (结果个数 = 1)
  ```
- 查询所有的UPF服务区域信息。 LST UPAREA:;
  ```
  %%LST UPAREA:;%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  UPF服务区名称  UPF服务区类型

  iuarea1        23G LAI    
  n2area1        5G TAI     
  n2area2        5G TAI     
  s1area1001     4G TAI     
  uparea1        4G TAI     
  (结果个数 = 5)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UPF服务区（LST-UPAREA）_09651370.md`
