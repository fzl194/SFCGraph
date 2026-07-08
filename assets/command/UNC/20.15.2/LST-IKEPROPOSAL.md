---
id: UNC@20.15.2@MMLCommand@LST IKEPROPOSAL
type: MMLCommand
name: LST IKEPROPOSAL（查询IKE提议）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IKEPROPOSAL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IKE安全提议
status: active
---

# LST IKEPROPOSAL（查询IKE提议）

## 功能

该命令用于查询IKE安全提议配置。

## 注意事项

通过软参方式配置不安全算法MD5、DES、3DES时， [**LST IKEPROPOSAL**](查询IKE提议（LST IKEPROPOSAL）_25830693.md) 命令显示仍为该命令原先配置的算法，不会显示MD5或DES或3DES。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROPOSALNUMBER | 安全提议号 | 可选必选说明：可选参数<br>参数含义：提议编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295。101不支持配置，但可以查询。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IKEPROPOSAL]] · IKE提议（IKEPROPOSAL）

## 使用实例

查询IKE安全提议号为1的IKE安全提议：

```
LST IKEPROPOSAL:PROPOSALNUMBER=1;
RETCODE = 0  操作成功

结果如下
-------------------------
     安全提议号  =  1
       认证方法  =  预共享
       认证算法  =  Sha2-256算法
       加密算法  =  256位AES算法
     完整性算法  =  Sha2-256算法
           DH组  =  无
重认证间隔（s）  =  86400
SA持续长度（s）  =  86400
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IKEPROPOSAL.md`
