---
id: UNC@20.15.2@MMLCommand@LST SMSCGT
type: MMLCommand
name: LST SMSCGT（查询SMSC的GT）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSCGT
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- SMSC选择管理
status: active
---

# LST SMSCGT（查询SMSC的GT）

## 功能

**适用NF：SMSF**

该命令用于查询所有配置的SMSC GT。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GT | SMSC的GT | 可选必选说明：可选参数<br>参数含义：该参数用于表示SMSC的GT。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSCGT]] · SMSC的GT（SMSCGT）

## 使用实例

当运营商需要查询所有配置的SMSC GT时，执行以下命令：

```
LST SMSCGT:;
%%LST SMSCGT:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
SMSC的全局名 = 123456
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSCGT.md`
