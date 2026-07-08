---
id: UNC@20.15.2@MMLCommand@LST CONFLICTIP
type: MMLCommand
name: LST CONFLICTIP（查询冲突地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CONFLICTIP
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 冲突地址管理
status: active
---

# LST CONFLICTIP（查询冲突地址）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用来查询指定本地地址池中的冲突地址。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定已配置的地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CONFLICTIP]] · 冲突地址（CONFLICTIP）

## 使用实例

查询本地地址池lap中配置的冲突地址，POOLNAME为“lap”： LST CONFLICTIP:POOLNAME="lap";

```
%%LST CONFLICTIP:POOLNAME="lap";%%
RETCODE = 0  操作成功。

结果如下
--------------
地址池名称 =  lap
IP地址类型 =  IPv4
冲突IPv4地址  =  10.1.1.1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CONFLICTIP.md`
