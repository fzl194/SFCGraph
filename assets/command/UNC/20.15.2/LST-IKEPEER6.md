---
id: UNC@20.15.2@MMLCommand@LST IKEPEER6
type: MMLCommand
name: LST IKEPEER6（查询IPv6 IKE对等体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IKEPEER6
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IKE对等体IPv6
status: active
---

# LST IKEPEER6（查询IPv6 IKE对等体）

## 功能

该命令用于查询IKE对等体。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERNAME | IKE对等体名称 | 可选必选说明：可选参数<br>参数含义：对端名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IPv6 IKE对等体（IKEPEER6）](configobject/UNC/20.15.2/IKEPEER6.md)

## 使用实例

查询名称为“peer1”的IKE对等体：

```
LST IKEPEER6:;
RETCODE = 0 操作成功

结果如下
-------------------------
         IKE对等体名称   = peer1
             预共享密钥  =  *****
               交换模式  =  Main
                 Nat穿越 = TRUE
               安全提议  =  101
             本地ID类型  =  IPv6
                 远端ID  =  NULL
                  版本1  =  TRUE
                  版本2  =  TRUE
               远端地址  =  ::
          SA绑定VPN名称  =  NULL
        远端地址VPN名称  =  NULL
             证书文件名  =  NULL
           低位认证地址  =  ::
           高位认证地址  =  ::
            DPD载荷顺序  =  DPD payload order hash first and then notify
  使能IKE消息序列号同步  =  Enable
使能IPSEC消息序列号同步  =  Enable
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IPv6-IKE对等体（LST-IKEPEER6）_21521230.md`
