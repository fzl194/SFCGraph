---
id: UNC@20.15.2@MMLCommand@LST LOCALAPNNIGP
type: MMLCommand
name: LST LOCALAPNNIGP（查询本地APNNI组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCALAPNNIGP
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 本地APNNI组管理
status: active
---

# LST LOCALAPNNIGP（查询本地APNNI组）

## 功能

**适用网元：SGSN**

该命令用于查询本地APNNI组信息。定制APN纠正功能会引用该配置参数APNNIGRPID，可参考 **[ADD SMACTCTRL](../激活过程管理/增加激活过程控制参数（ADD SMACTCTRL）_26305472.md)** 命令的APNNIGRPID参数说明。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [本地APNNI组（LOCALAPNNIGP）](configobject/UNC/20.15.2/LOCALAPNNIGP.md)

## 使用实例

查询LOCALAPNNI组信息。

LST LOCALAPNNIGP:;

```
%%LST LOCALAPNNIGP:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
本地APNNI组号  =  1
        APNNI  =  HUAWEI1.COM
  APNNI优先级  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询本地APNNI组(LST-LOCALAPNNIGP)_80957788.md`
