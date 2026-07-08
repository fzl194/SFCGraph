---
id: UNC@20.15.2@MMLCommand@LST GLOBALIMS
type: MMLCommand
name: LST GLOBALIMS（查询全局IMS互通配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLOBALIMS
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- IMS业务功能
- 全局IMS配置
status: active
---

# LST GLOBALIMS（查询全局IMS互通配置信息）

## 功能

**适用NF：PGW-C、SMF、GGSN、SGW-C**

该命令用于查询全局IMS配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLOBALIMS]] · 全局IMS互通配置信息（GLOBALIMS）

## 使用实例

显示全局IMS配置：

```
%%LST GLOBALIMS:;%%
RETCODE = 0  操作成功

全局IMS配置信息
------------------------
                        IMS功能开关  =  使能
                IMS信令空口增强开关  =  使能
                  缺省IPv4 P-CSCF组  =  pcsf1
                  缺省IPv6 P-CSCF组  =  NULL
            发送更新消息速率(个/秒)  =  1000
          缺省IPv4 P-CSCF组域名开关  =  使能
          缺省IPv6 P-CSCF组域名开关  =  不使能
基于UDM的P-CSCF Restoration功能开关  =  不使能
基于UDM的P-CSCF Restoration功能模式  =  PDU会话重激活
基于HSS的P-CSCF Restoration功能开关  =  不使能
基于HSS的P-CSCF Restoration功能模式  =  PDU会话重激活
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GLOBALIMS.md`
