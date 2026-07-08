---
id: UDG@20.15.2@MMLCommand@DSP LDPBFDTNNLSESSION
type: MMLCommand
name: DSP LDPBFDTNNLSESSION（显示BFD For LDP Tunnel的BFD会话）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LDPBFDTNNLSESSION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- BFD For LDP Tunnel的BFD会话
status: active
---

# DSP LDPBFDTNNLSESSION（显示BFD For LDP Tunnel的BFD会话）

## 功能

该命令用于显示BFD For LDP Tunnel的BFD会话信息。

## 注意事项

查询会话类型为LDP隧道会话的BFD会话，只有在主动端才能查询到BFD会话信息，在被动端需要通过DSP BFDSESSION查询BFD会话信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FECADDRESS | FEC地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示BFD For LDP Tunnel的FEC地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LDPBFDTNNLSESSION]] · BFD For LDP Tunnel的BFD会话（LDPBFDTNNLSESSION）

## 使用实例

显示BFD For LDP Tunnel的BFD会话信息：

```
DSP LDPBFDTNNLSESSION:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                    FEC地址  =  192.168.1.1
                    LSP索引  =  5000004
        BFD会话的本地标识符  =  16385
                   会话状态  =  Down状态
         最小发送间隔（ms）  =  0
         最小接收间隔（ms）  =  0
                   检测倍数  =  0
          会话建立时长（s）  =  20079
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-LDPBFDTNNLSESSION.md`
