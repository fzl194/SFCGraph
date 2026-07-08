---
id: UDG@20.15.2@MMLCommand@LST HOST
type: MMLCommand
name: LST HOST（查询Host）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HOST
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 主机名
status: active
---

# LST HOST（查询Host）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询指定Host信息或所有Host信息。

## 注意事项

输入HostName查询匹配记录，不输入HostName查询所有记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | Host配置名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HOST配置名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [Host（HOST）](configobject/UDG/20.15.2/HOST.md)

## 使用实例

查询所有的HOST记录：

```
LST HOST:;
```

```

RETCODE = 0  操作成功。

Host信息
--------
Host配置名称  =  huawei
        域名  =  www.huawei.com
      优先级  =  10086
  配置域名称  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Host（LST-HOST）_82837325.md`
