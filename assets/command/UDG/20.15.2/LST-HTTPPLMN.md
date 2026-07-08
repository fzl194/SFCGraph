---
id: UDG@20.15.2@MMLCommand@LST HTTPPLMN
type: MMLCommand
name: LST HTTPPLMN（查询HTTP服务存储的PLMN）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HTTPPLMN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP平台管理
status: active
---

# LST HTTPPLMN（查询HTTP服务存储的PLMN）

## 功能

该命令用以查询HTTP服务存储的PLMN。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数唯一标识某个运营商。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成HTTP PLMN的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成HTTP PLMN的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HTTPPLMN]] · HTTP服务存储的PLMN（HTTPPLMN）

## 使用实例

- 查询指定HTTP服务存储的PLMN，执行如下命令：
  ```
  %%LST HTTPPLMN: NOID=0, MCC="460", MNC="210";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  运营商标识  =  0
  移动国家码  =  460
    移动网号  =  210
    描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询系统配置的HTTP服务存储的PLMN，执行如下命令：
  ```
  %%LST HTTPPLMN:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  运营商标识  移动国家码  移动网号  描述信息  

  0           460         03        NULL         
  0           460         210       NULL         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-HTTPPLMN.md`
