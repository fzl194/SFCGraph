---
id: UDG@20.15.2@MMLCommand@LST LDPINSTANCE
type: MMLCommand
name: LST LDPINSTANCE（查询LDP实例配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LDPINSTANCE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP实例
status: active
---

# LST LDPINSTANCE（查询LDP实例配置）

## 功能

该命令用于查询LDP实例配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [LDP实例（LDPINSTANCE）](configobject/UDG/20.15.2/LDPINSTANCE.md)

## 使用实例

查询LDP实例配置：

```
LST LDPINSTANCE:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                 VPN实例名称  =  _public_
                实例的LSR ID  =  192.168.1.11
        IGP联动延迟时间（s）  =  10
                优雅删除标志  =  FALSE
           优雅删除时间（s）  =  5
禁止向remote-peer发送mapping  =  FALSE
             LDP全局认证模式  =  配置认证
             LDP全局认证类型  =  KeyChain认证类型
         LDP全局KeyChain名字  =  bbb
              LDP全局MD5密码  =  NULL
                    水平分割  =  FALSE
        发送所有loopback地址  =  FALSE
                标签控制模式  =  Ordered
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询LDP实例配置（LST-LDPINSTANCE）_49802210.md`
