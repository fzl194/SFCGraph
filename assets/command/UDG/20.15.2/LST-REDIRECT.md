---
id: UDG@20.15.2@MMLCommand@LST REDIRECT
type: MMLCommand
name: LST REDIRECT（查询重定向）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: REDIRECT
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- URL重定向控制
- 重定向
status: active
---

# LST REDIRECT（查询重定向）

## 功能

**适用NF：PGW-U、UPF**

此命令用于运营商查询已经配置的URL重定向策略，可以查询重定向携带信息名称等。

## 注意事项

输入REDIRECTNAME查询指定记录，如果不输入REDIRECTNAME表示查询所有记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REDIRECTNAME | 重定向名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置重定向配置名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/REDIRECT]] · 重定向（REDIRECT）

## 使用实例

查询名为testredirect2的URL重定向策略：

```
LST REDIRECT:REDIRECTNAME="testredirect2";
```

```

RETCODE = 0  操作成功。

重定向信息
----------
        重定向名称  =  testredirect2
               URL  =  www.huawei.com
          流控标识  =  不使能
流控时间间隔（秒）  =  5
    重定向缺省动作  =  BLOCK
重定向携带信息名称  =  test
        配置域名称  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询重定向（LST-REDIRECT）_82837531.md`
