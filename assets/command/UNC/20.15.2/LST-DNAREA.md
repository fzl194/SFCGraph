---
id: UNC@20.15.2@MMLCommand@LST DNAREA
type: MMLCommand
name: LST DNAREA（查询DNAI服务区域）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNAREA
command_category: 查询类
applicable_nf:
- SGW-C
- SMF
- GGSN
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- DNAI位置绑定区域管理
status: active
---

# LST DNAREA（查询DNAI服务区域）

## 功能

**适用NF：SGW-C、SMF、GGSN、PGW-C**

该命令用于查询DNAI服务区域。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | DNAI服务区域名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置DNAI服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNAI服务区域（DNAREA）](configobject/UNC/20.15.2/DNAREA.md)

## 使用实例

- 查询区域名称为"DNAREA1"的DNAI服务区域信息。 LST DNAREA: AREANAME="DNAREA1";
  ```
  %%LST DNAREA:AREANAME="DNAREA1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  DNAI服务区域名称  =  dnarea1
  DNAI服务区域类型  =  5G类型的TAI
  (结果个数 = 1)
  ```
- 查询所有的DNAI服务区域信息。 LST DNAREA:;
  ```
  %%LST DNAREA:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  DNAI服务区域名称  DNAI服务区域类型  

  dnarea1           5G类型的TAI       
  dnarea2           5G类型的Cell Id   
  (结果个数 = 2)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNAI服务区域（LST-DNAREA）_71516433.md`
