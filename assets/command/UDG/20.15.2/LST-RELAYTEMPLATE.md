---
id: UDG@20.15.2@MMLCommand@LST RELAYTEMPLATE
type: MMLCommand
name: LST RELAYTEMPLATE（查询媒体中继模板）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYTEMPLATE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继模板
status: active
---

# LST RELAYTEMPLATE（查询媒体中继模板）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询媒体中继模板。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYTPLNAME | 媒体中继模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定媒体中继模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYTEMPLATE]] · 媒体中继模板（RELAYTEMPLATE）

## 使用实例

假如需要查询一组媒体中继模板，则命令如下：

```
LST RELAYTEMPLATE:RELAYTPLNAME="test";
```

```

RETCODE = 0  操作成功
 
结果如下
------------------------
              媒体中继模板名称  =  test
                   DNS规范名称  =  testcname
             DNS存活时间（秒）  =  180
              DNS IP不匹配操作  =  返回未找到
                   TLS配置名称  =  NULL
        UE访问未知域名处理动作  =  重定向
                        厂商ID  =  2
      媒体文件老化时间（小时）  =  168
媒体文件有效性校验时长（分钟）  =  15
        媒体文件有效性校验方式  =  GET请求方式
        媒体属性更新时间（秒）  =  60
                    配置域名称  =  testDomain
(结果个数 = 1)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询媒体中继模板（LST-RELAYTEMPLATE）_14777347.md`
