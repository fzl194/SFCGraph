---
id: UDG@20.15.2@MMLCommand@LST UACINFO
type: MMLCommand
name: LST UACINFO（显示UAC信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UACINFO
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 专网策略配置
- UAC信息
status: active
---

# LST UACINFO（显示UAC信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询UAC服务器的地址信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UACNAME | UAC名称 | 可选必选说明：可选参数<br>参数含义：UAC名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UACINFO]] · UAC信息（UACINFO）

## 使用实例

查询UAC服务器的地址信息：

```
LST UACINFO: UACNAME="test";
```

```

RETCODE = 0  Operation succeeded

UAC Information
---------------
        UAC Name  =  test
UAC IPv4 Address  =  192.168.0.10
UAC IPv6 Address  =  ::
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示UAC信息（LST-UACINFO）_28486283.md`
