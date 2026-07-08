---
id: UNC@20.15.2@MMLCommand@LST NRFNOTNOTIFYNF
type: MMLCommand
name: LST NRFNOTNOTIFYNF（查询不通知NF实例）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFNOTNOTIFYNF
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF通知管理
status: active
---

# LST NRFNOTNOTIFYNF（查询不通知NF实例）

## 功能

**适用NF：NRF**

该命令用于查询不通知的NF实例列表。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：<br>该命令与SET NRFNOTIFYPLY配合使用，当SET NRFNOTIFYPLY中的NOTIFYNPLY参数设置为“NFINSTANCEIDNOT”时生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNOTNOTIFYNF]] · 不通知NF实例（NRFNOTNOTIFYNF）

## 使用实例

- 查询不通知NF列表中的所有NF实例标识，执行如下命令。
  ```
  LST NRFNOTNOTIFYNF:;
  %%LST NRFNOTNOTIFYNF:;%%
  RETCODE = 0  操作成功

  结果如下
  ---------
  NF实例标识  

  88888888-4444-1234-5678-123456789abc
  88888888-6666-1234-5678-123456789abc
  (结果个数 = 2)

  ---    END
  ```
- 查询实例标识为"88888888-4444-1234-5678-123456789abc"的NF是否在不通知NF列表中，执行如下命令。
  ```
  LST NRFNOTNOTIFYNF:NFINSTANCEID="88888888-4444-1234-5678-123456789abc";
  %%LST NRFNOTNOTIFYNF:NFINSTANCEID="88888888-4444-1234-5678-123456789abc";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  NF实例标识  =  88888888-4444-1234-5678-123456789abc
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询不通知NF实例（LST-NRFNOTNOTIFYNF）_07330082.md`
