---
id: UNC@20.15.2@MMLCommand@LST BSFAPNGROUP
type: MMLCommand
name: LST BSFAPNGROUP（查询APN组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BSFAPNGROUP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- BSF信息管理
status: active
---

# LST BSFAPNGROUP（查询APN组）

## 功能

该命令用于查询APN组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPNAME | APN组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BSFAPNGROUP]] · APN组（BSFAPNGROUP）

## 使用实例

查询APN组"apngroup1"中的APN信息：

```
%%LST BSFAPNGROUP: GRPNAME="apngroup1";%%
RETCODE = 0  操作成功

结果如下
--------
APN组名  =  apngroup1
APN名称  =  huawei.com
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN组（LST-BSFAPNGROUP）_21742341.md`
