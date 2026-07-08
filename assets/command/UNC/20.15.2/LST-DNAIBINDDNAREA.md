---
id: UNC@20.15.2@MMLCommand@LST DNAIBINDDNAREA
type: MMLCommand
name: LST DNAIBINDDNAREA（查询DNAI支持的服务区域）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNAIBINDDNAREA
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

# LST DNAIBINDDNAREA（查询DNAI支持的服务区域）

## 功能

**适用NF：SGW-C、SMF、GGSN、PGW-C**

该命令用于查询DNAI支持的服务区域信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNAIBINDDNAREA]] · DNAI支持的服务区域（DNAIBINDDNAREA）

## 使用实例

- 查询数据网络访问标识为"ulcl"的区域绑定的服务区域。 LST DNAIBINDDNAREA: DNAI="ulcl";
  ```
  %%LST DNAIBINDDNAREA: DNAI="ulcl";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  数据网络访问标识  DNAI服务区域名称  

  ulcl              dnarea1           
  ulcl              dnarea2           
  (结果个数 = 2)
  ```
- 查询所有数据网络访问标识绑定的服务区域。 LST DNAIBINDDNAREA:;
  ```
  %%LST DNAIBINDDNAREA:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  数据网络访问标识  DNAI服务区域名称  

  ulcl              dnarea1           
  ulcl              dnarea2           
  bp                dnarea3           
  (结果个数 = 3)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DNAIBINDDNAREA.md`
