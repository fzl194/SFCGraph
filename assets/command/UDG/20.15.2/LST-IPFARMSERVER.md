---
id: UDG@20.15.2@MMLCommand@LST IPFARMSERVER
type: MMLCommand
name: LST IPFARMSERVER（查询IPFarmServer）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPFARMSERVER
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- IP Farm 管理
- IP Farm服务器
status: active
---

# LST IPFARMSERVER（查询IPFarmServer）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示该IP farm服务器所在的IP farm中的所有IP farm服务器信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPFARMNAME | IP-Farm名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IP farm名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IPFarmServer（IPFARMSERVER）](configobject/UDG/20.15.2/IPFARMSERVER.md)

## 使用实例

查询一个IP farm下的全部服务器：

```
LST IPFARMSERVER:;
```

```

RETCODE = 0  操作成功。

IPFarmServer信息
----------------
       IP-Farm名称  =  test
          地址信息  =  10.0.0.1
               URL  =  www.huawei.com
    重定向缺省动作  =  BLOCK
重定向携带信息名称  =  test
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPFarmServer（LST-IPFARMSERVER）_82837059.md`
