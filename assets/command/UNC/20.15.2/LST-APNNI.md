---
id: UNC@20.15.2@MMLCommand@LST APNNI
type: MMLCommand
name: LST APNNI（查询APNNI）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNNI
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- APNNI信息管理
- APNNI管理
status: active
---

# LST APNNI（查询APNNI）

## 功能

**适用网元：SGSN、MME**

该命令用来查询APNNI组成员信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPID | APNNI组号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APNNI组号。<br>数据来源：本端规划<br>取值范围：0～15<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNNI]] · APNNI（APNNI）

## 使用实例

查询APNNI组成员信息：

LST APNNI:;

```
%%LST APNNI:;%%
输出结果如下
--------------
APNNI组号  =  2
    APNNI  =  HUAWEI.COM
     描述  =  noname
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNNI.md`
