---
id: UDG@20.15.2@MMLCommand@RMV BWMUSERGRPALL
type: MMLCommand
name: RMV BWMUSERGRPALL（删除所有带宽管理用户组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: BWMUSERGRPALL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理用户组
status: active
---

# RMV BWMUSERGRPALL（删除所有带宽管理用户组）

## 功能

**适用NF：PGW-U、UPF**

![](删除所有带宽管理用户组（RMV BWMUSERGRPALL）_08574047.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，会删除带宽管理用户组下所有绑定关系。

该命令用于删除所有的带宽管理用户组。当运营商希望删除已配置的默认用户组或具体用户组时，则执行该命令。

## 注意事项

- 删除一个带宽管理用户组，对已在线用户的用户级TOS业务立即生效，而用户更新才会触发删除的配置对其他业务生效。
- 删除一个带宽管理用户组会同时删除该用户组下所有的带宽管理规则和与APN、UserProfile的绑定关系。
- 全局用户组为系统默认配置，不能删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/BWMUSERGRPALL]] · 所有带宽管理用户组（BWMUSERGRPALL）

## 使用实例

假如运营商需要删除所有的带宽管理业务：

```
RMV BWMUSERGRPALL:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除所有带宽管理用户组（RMV-BWMUSERGRPALL）_08574047.md`
