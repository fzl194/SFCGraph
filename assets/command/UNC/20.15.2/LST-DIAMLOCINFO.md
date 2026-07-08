---
id: UNC@20.15.2@MMLCommand@LST DIAMLOCINFO
type: MMLCommand
name: LST DIAMLOCINFO（查询Diameter本端信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DIAMLOCINFO
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- Diameter本端信息
status: active
---

# LST DIAMLOCINFO（查询Diameter本端信息）

## 功能

**适用NF：PGW-C、SMF**

此命令用来查询Diameter本端信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 本端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DIAMLOCINFO]] · Diameter本端信息（DIAMLOCINFO）

## 使用实例

查询HOSTNAME为“test”的Diameter本端信息：

```
LST DIAMLOCINFO: HOSTNAME="test";
```

```

RETCODE = 0  操作成功

Diameter本端主机信息
--------------------
             本端主机名  =  test
               本端域名  =  test
               产品名称  =  product
        Vendor-Id AVP值  =  0
 Firmware-RevisionAVP值  =  1
    Origin-State-Id AVP  =  不使能
Supported-Vendor-Id AVP  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DIAMLOCINFO.md`
