---
id: UNC@20.15.2@MMLCommand@LST LDPPEERPOLICY
type: MMLCommand
name: LST LDPPEERPOLICY（查询LDP邻居策略配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LDPPEERPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP邻居策略
status: active
---

# LST LDPPEERPOLICY（查询LDP邻居策略配置）

## 功能

该命令用于查询配置的LDP邻居策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| PEERID | 对等体的LSR ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定对等体的LSR ID。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LDPPEERPOLICY]] · LDP邻居策略（LDPPEERPOLICY）

## 使用实例

查询LDP邻居策略：

```
LST LDPPEERPOLICY:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
               VPN实例名称  =  _public_
            对等体的LSR ID  =  192.168.1.1
               LDP认证模式  =  配置认证
               LDP认证类型  =  KeyChain认证类型
                   MD5密码  =  NULL
              KeyChain名字  =  key1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LDPPEERPOLICY.md`
