---
id: UNC@20.15.2@MMLCommand@LST SMCAUSEGRP
type: MMLCommand
name: LST SMCAUSEGRP（查询SM原因值映射组配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMCAUSEGRP
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- SM原因值管理
- 原因值映射组管理
status: active
---

# LST SMCAUSEGRP（查询SM原因值映射组配置）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于查询原因值映射组配置记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CAUSEGRPID | 原因值组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定表示一个原因值映射规则集合的唯一数字ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMCAUSEGRP]] · SM原因值映射组配置（SMCAUSEGRP）

## 使用实例

查询原因值映射组配置：参数原因值组标识设置为126。 LST SMCAUSEGRP: CAUSEGRPID=126;

```
%%LST SMCAUSEGRP: CAUSEGRPID=126;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
原因值组标识  =  126
原因值组名称  =  aaa
（结果个数 = 1）

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMCAUSEGRP.md`
