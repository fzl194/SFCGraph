---
id: UNC@20.15.2@MMLCommand@LST UPLIST4RDS
type: MMLCommand
name: LST UPLIST4RDS（查询RADIUS服务器使用的UP列表配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPLIST4RDS
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- UP列表
status: active
---

# LST UPLIST4RDS（查询RADIUS服务器使用的UP列表配置）

## 功能

**适用NF：PGW-C、SMF**

LST UPLIST4RDS命令用来查询UP列表配置，该UPF列表用于根据UP选择RADIUS服务器发送RADIUS消息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPLISTNAME | UP列表名称 | 可选必选说明：可选参数<br>参数含义：指定UP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。长度1到63的非空格字符串。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPLIST4RDS]] · 从RADIUS服务器使用的UP列表中删除UP（UPLIST4RDS）

## 使用实例

显示名为“uplist1”的UP列表下的UP的配置信息：

```
LST UPLIST4RDS: UPLISTNAME="uplist1";
```

```

RETCODE = 0  操作成功

UPF列表信息
-----------
UP列表名称  =  uplist1
UP实例标识  =  up1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RADIUS服务器使用的UP列表配置（LST-UPLIST4RDS）_52749062.md`
