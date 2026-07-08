---
id: UNC@20.15.2@MMLCommand@DSP SSHCCONNSTC
type: MMLCommand
name: DSP SSHCCONNSTC（显示客户端的连接统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SSHCCONNSTC
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

# DSP SSHCCONNSTC（显示客户端的连接统计信息）

## 功能

该命令用于显示SSH客户端连接统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [客户端的连接统计信息（SSHCCONNSTC）](configobject/UNC/20.15.2/SSHCCONNSTC.md)

## 使用实例

显示SSH客户端连接统计信息：

```
DSP SSHCCONNSTC:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
                          总连接数  =  22
                        SFTP会话数  =  1
                    SNetconf会话数  =  0
                     STelnet会话数  =  1
                         MML会话数  =  10
                     MML关闭连接数  =  9
                     CLI关闭连接数  =  0
                SNetconf关闭连接数  =  0
                    SSHS关闭连接数  =  0
                  Socket关闭连接数  =  1
                  CTRL+T关闭连接数  =  0
                  CTRL+]关闭连接数  =  0
                    鉴权关闭连接数  =  0
                     ACL拒绝连接数  =  0
                  Socket创建失败数  =  2
                 Channel失败连接数  =  0
                 Channel关闭连接数  =  0
                        断连消息数  =  0
                        在线连接数  =  4
                          重传次数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示客户端的连接统计信息（DSP-SSHCCONNSTC）_00841345.md`
