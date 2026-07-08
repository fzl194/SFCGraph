---
id: UNC@20.15.2@MMLCommand@LST USRCTLGGSN
type: MMLCommand
name: LST USRCTLGGSN（查询手工恢复GGSN地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USRCTLGGSN
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GGSN容灾功能
status: active
---

# LST USRCTLGGSN（查询手工恢复GGSN地址）

## 功能

**适用网元：SGSN**

此命令用于查询配置的手工恢复GGSN地址。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRCTLGGSN]] · 手工恢复GGSN地址（USRCTLGGSN）

## 使用实例

查询配置的手工恢复GGSN地址列表：

LST USRCTLGGSN:;

```
%%LST USRCTLGGSN:;%%
RETCODE = 0  操作成功。

输出结果如下
----------------
 IP地址类型  =  IPv4
   IPv4地址  =  192.168.123.123
       描述  =  123
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-USRCTLGGSN.md`
