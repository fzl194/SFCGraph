---
id: UDG@20.15.2@MMLCommand@DSP LDPLSP
type: MMLCommand
name: DSP LDPLSP（显示LDP LSP）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LDPLSP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP LSP
status: active
---

# DSP LDPLSP（显示LDP LSP）

## 功能

该命令用于显示LDP LSP。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| LSPADDR | 目的地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示目的地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：当“PREFIXLENGTH”参数被输入的时候，该参数也必须输入。 |
| PREFIXLENGTH | 前缀长度 | 可选必选说明：可选参数<br>参数含义：该参数用于表示目的地址的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：当“LSPADDR”参数被输入的时候，该参数也必须输入。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LDPLSP]] · LDP LSP（LDPLSP）

## 使用实例

显示LDP LSP：

```
DSP LDPLSP:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
        VPN实例名称  =  _public_
           目的地址  =  192.168.1.1
           前缀长度  =  32
            LSP索引  =  5000001
          LSP下一跳  =  192.168.0.2
             入标签  =  3
             出标签  =  NULL
             出接口  =  LoopBack100
            LSP类型  =  出节点
          LSP MTU值  =  NULL
            FRR LSP  =  FALSE
           RLFA LSP  =  FALSE
 LSP建立的时长（s）  =  545
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-LDPLSP.md`
