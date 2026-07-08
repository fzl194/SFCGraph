---
id: UNC@20.15.2@MMLCommand@LST SELCHFGBYIMSI
type: MMLCommand
name: LST SELCHFGBYIMSI（查询IMSI与CHF组的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SELCHFGBYIMSI
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- CHF选择
status: active
---

# LST SELCHFGBYIMSI（查询IMSI与CHF组的绑定关系）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询IMSI与CHF组的绑定关系。

## 注意事项

不输入任何参数默认查询所有配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 用户的IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于设置绑定的IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是14~15。<br>默认值：无<br>配置原则：<br>该参数表示用户完整的IMSI信息，不支持前缀匹配。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SELCHFGBYIMSI]] · IMSI与CHF组的绑定关系（SELCHFGBYIMSI）

## 使用实例

- 查询基于IMSI选择CHF处理:
  ```
  %%LST SELCHFGBYIMSI: IMSI="123456789012345";%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  用户的IMSI  =  123456789012345
  主CHF组  =  CHF1
  备CHF组  =  CHF2
  (结果个数 = 1)

  ---    END
  ```
- 查询所有配置:
  ```
  %%LST SELCHFGBYIMSI:;%%
  RETCODE = 0  操作成功。

  结果如下
  ------------------------
  用户的IMSI       主CHF组  备CHF组

  123456789012345  CHF1     CHF2
  223456789012345  CHF1     CHF2
  323456789012345  CHF1     CHF2
  (结果个数 = 3)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SELCHFGBYIMSI.md`
