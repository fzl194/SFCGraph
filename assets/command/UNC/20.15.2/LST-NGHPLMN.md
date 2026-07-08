---
id: UNC@20.15.2@MMLCommand@LST NGHPLMN
type: MMLCommand
name: LST NGHPLMN（查询5G Home PLMN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGHPLMN
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- SGW-C
- PGW-C
- GGSN
- NSSF
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- Home PLMN信息管理
status: active
---

# LST NGHPLMN（查询5G Home PLMN）

## 功能

**适用NF：AMF、SMF、NRF、SGW-C、PGW-C、GGSN、NSSF、SMSF**

该命令用以查询配置的Home PLMN。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于唯一标识某个运营商。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成Home PLMN的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成Home PLMN的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G Home PLMN（NGHPLMN）](configobject/UNC/20.15.2/NGHPLMN.md)

## 使用实例

- 查询指定运营商的Home PLMN列表，执行如下命令：
  ```
  %%LST NGHPLMN: NOID=0, MCC="123", MNC="210";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  运营商标识  =  0
  移动国家码  =  123
    移动网号  =  210
    描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询系统配置的运营商Home PLMN列表，执行如下命令：
  ```
  %%LST NGHPLMN:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  运营商标识  移动国家码  移动网号  描述信息  

  0           123         03        NULL         
  0           123         210       NULL         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G-Home-PLMN（LST-NGHPLMN）_09653743.md`
