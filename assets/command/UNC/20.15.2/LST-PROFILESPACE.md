---
id: UNC@20.15.2@MMLCommand@LST PROFILESPACE
type: MMLCommand
name: LST PROFILESPACE（查询Profile Space）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PROFILESPACE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- Profile Space
status: active
---

# LST PROFILESPACE（查询Profile Space）

## 功能

**适用NF：PGW-C、SMF**

本命令用于查询配置的Profile Space实例。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROFSPACENAME | Profile Space名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ProfileSpace名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PROFILESPACE]] · Profile Space（PROFILESPACE）

## 使用实例

查询ProfileSpace配置，PROFSPACENAME为“profilespace1”：

```
LST PROFILESPACE:PROFSPACENAME="profilespace1";
```

```

RETCODE = 0  操作成功

Profile Space 信息
------------------
Always Allowed Profile名称  =  userprofile1
         Profile Space名称  =  profilespace1
                拼接开关  =  ENABLE
                拼接字符串  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Profile-Space（LST-PROFILESPACE）_09897050.md`
