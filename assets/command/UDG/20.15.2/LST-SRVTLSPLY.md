---
id: UDG@20.15.2@MMLCommand@LST SRVTLSPLY
type: MMLCommand
name: LST SRVTLSPLY（查询TLS认证策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SRVTLSPLY
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- TLS认证策略
status: active
---

# LST SRVTLSPLY（查询TLS认证策略）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询TLS认证策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置TLS认证策略描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVTLSPLY]] · TLS认证策略（SRVTLSPLY）

## 使用实例

查询TLS认证策略：

```
LST SRVTLSPLY:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
   策略名称  =  ply1
   实体类型  =  客户端
   协议版本  =  传输层安全性协议版本v1.2
加密套件集合  =  TLS_DHE_RSA_WITH_AES128_GCM_SHA256
设备证书场景  =  sc_ne
 CA证书场景  =  sc_ca
验证对端证书  =  开启校验对端证书
   校验深度  =  100
吊销证书列表  =  关闭吊销证书列表
  配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TLS认证策略（LST-SRVTLSPLY）_43992596.md`
