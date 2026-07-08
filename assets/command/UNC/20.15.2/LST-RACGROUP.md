---
id: UNC@20.15.2@MMLCommand@LST RACGROUP
type: MMLCommand
name: LST RACGROUP（查询RAC组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RACGROUP
command_category: 查询类
applicable_nf:
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 虚拟APN映射管理
- 基于RAC位置的虚拟APN映射管理
- 虚拟APN映射的RAC组
status: active
---

# LST RACGROUP（查询RAC组）

## 功能

**适用NF：GGSN**

该命令用来查看指定RAC组或者所有RAC组的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RACGROUPNAME | RAC组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [RAC组（RACGROUP）](configobject/UNC/20.15.2/RACGROUP.md)

## 使用实例

假设运营商需要去查询指定“RAC组名”为“beijing”的RAC组：

```
LST RACGROUP: RACGROUPNAME="beijing";
RETCODE = 0  操作成功。

结果如下
-------------
指定RAC组名  =  beijing
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RAC组（LST-RACGROUP）_09651778.md`
