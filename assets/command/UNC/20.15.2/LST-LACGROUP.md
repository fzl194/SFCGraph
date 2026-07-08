---
id: UNC@20.15.2@MMLCommand@LST LACGROUP
type: MMLCommand
name: LST LACGROUP（查询LAC组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LACGROUP
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
- 基于LAC位置的虚拟APN映射管理
- 虚拟APN映射的LAC组
status: active
---

# LST LACGROUP（查询LAC组）

## 功能

**适用NF：GGSN**

该命令用来查看指定LAC组或者所有LAC组的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACGROUPNAME | LAC组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LACGROUP]] · LAC组（LACGROUP）

## 使用实例

假设运营商需要去查询指定“LAC组名”为“beijing”的LAC组：

```
LST LACGROUP: LACGROUPNAME="beijing";
RETCODE = 0  操作成功。

结果如下
--------
指定LAC组名  =  beijing
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LACGROUP.md`
