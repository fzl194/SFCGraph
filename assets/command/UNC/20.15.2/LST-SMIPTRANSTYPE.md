---
id: UNC@20.15.2@MMLCommand@LST SMIPTRANSTYPE
type: MMLCommand
name: LST SMIPTRANSTYPE（查询会话管理接口IP传输类型）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMIPTRANSTYPE
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- SM接口IP传输类型管理
status: active
---

# LST SMIPTRANSTYPE（查询会话管理接口IP传输类型）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用来查询会话管理接口IP传输类型。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMIPTRANSTYPE]] · 会话管理接口IP传输类型（SMIPTRANSTYPE）

## 使用实例

查询会话管理接口IP传输类型：

```
%%LST SMIPTRANSTYPE:;%%
RETCODE = 0  操作成功

结果如下
--------
       SGW S11控制面接口IP类型  =  根据对端能力选择IP类型
        SGW S1用户面接口IP类型  =  IPv4优先
        SGW S5控制面接口IP类型  =  IPv6优先
        SGW S5用户面接口IP类型  =  IPv4优先
        SGW S8控制面接口IP类型  =  IPv4优先
        SGW S8用户面接口IP类型  =  IPv4优先
        PGW S5控制面接口IP类型  =  根据对端能力选择IP类型
        PGW S5用户面接口IP类型  =  根据对端能力选择IP类型
        PGW S8控制面接口IP类型  =  IPv4优先
        PGW S8用户面接口IP类型  =  IPv4优先
              UPF N3接口IP类型  =  使用双栈
            I-UPF N9接口IP类型  =  使用双栈
I-UPF home routed N9接口IP类型  =  IPv4优先
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMIPTRANSTYPE.md`
