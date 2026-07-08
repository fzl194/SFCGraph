---
id: UNC@20.15.2@MMLCommand@LST USRPDPCAP
type: MMLCommand
name: LST USRPDPCAP（查询用户面PDP规格表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USRPDPCAP
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- 转发资源管理
- PDP资源管理
- 用户面PDP规格管理
status: active
---

# LST USRPDPCAP（查询用户面PDP规格表）

## 功能

**适用网元：SGSN**

该命令用于查询GTP用户面PDP规格表。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USRPDPCAP]] · 用户面PDP规格表（USRPDPCAP）

## 使用实例

查询用户面PDP规格表：

LST USRPDPCAP:;

```
%%LST USRPDPCAP:;%%
RETCODE = 0  执行成功。

输出结果如下
-------------------
      PDP数过载门限(%) = 85             
  PDP数过载恢复门限(%) = 80
      PDP数拥塞门限(%) = 95
  PDP数拥塞恢复门限(%) = 90

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-USRPDPCAP.md`
