---
id: UDG@20.15.2@MMLCommand@DSP SSHSCONNSTC
type: MMLCommand
name: DSP SSHSCONNSTC（显示服务器的连接统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SSHSCONNSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- SSH调测
status: active
---

# DSP SSHSCONNSTC（显示服务器的连接统计信息）

## 功能

该命令用于显示SSH服务器连接统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SSHSCONNSTC]] · 服务器的连接统计信息（SSHSCONNSTC）

## 使用实例

显示SSH服务器连接统计信息：

```
DSP SSHSCONNSTC:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
                                总连接数  =  4
                          认证失败连接数  =  0
                           ACL拒绝连接数  =  0
                服务类型不匹配拒绝连接数  =  0
                           CLI拒绝连接数  =  0
                      SNetconf拒绝连接数  =  0
                           CLI关闭连接数  =  0
                      SNetconf关闭连接数  =  0
                           MML关闭连接数  =  0
                        Socket关闭连接数  =  0
                        客户端拒绝连接数  =  0
                           AAA关闭连接数  =  0
                        客户端关闭连接数  =  0
                          用户关闭连接数  =  0
              因算法不匹配拒绝连接的次数  =  0
                      因IP锁定拒绝连接数  =  0
                              在线连接数  =  2
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SSHSCONNSTC.md`
