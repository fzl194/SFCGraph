---
id: UNC@20.15.2@MMLCommand@DSP MSSCOMMMSGPOOL
type: MMLCommand
name: DSP MSSCOMMMSGPOOL（查询通信消息池信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSCOMMMSGPOOL
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 通信管理统计查询
status: active
---

# DSP MSSCOMMMSGPOOL（查询通信消息池信息）

## 功能

该命令用于查询MSS的通信消息池信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MSSCOMMMSGPOOL]] · 通信消息池信息（MSSCOMMMSGPOOL）

## 使用实例

查询通信消息池信息：

```
DSP MSSCOMMMSGPOOL:RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
消息池ID   单元大小（byte）   单元数量   已用数量    申请次数   释放次数   泄露数量
0          4096               4096       1           1123       1123       0
1          512                4096       0           1024       1024       0
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MSSCOMMMSGPOOL.md`
