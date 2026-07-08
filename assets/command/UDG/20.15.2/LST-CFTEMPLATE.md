---
id: UDG@20.15.2@MMLCommand@LST CFTEMPLATE
type: MMLCommand
name: LST CFTEMPLATE（查询内容过滤模板）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CFTEMPLATE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 内容过滤模板配置
status: active
---

# LST CFTEMPLATE（查询内容过滤模板）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示内容过滤模板的配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFTEMPLATENAME | 内容过滤模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内容过滤模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CFTEMPLATE]] · 内容过滤模板（CFTEMPLATE）

## 使用实例

显示内容过滤模板的配置：

```
LST CFTEMPLATE:;
```

```

RETCODE = 0  操作成功
 
内容过滤模板信息
----------------
                           内容过滤模板名称  =  test
主用CONTENT_FILTERING类型的ICAP服务器组名称  =  srg
备用CONTENT_FILTERING类型的ICAP服务器组名称  =  NULL
                           响应超时限制次数  =  100
                       响应超时时间（毫秒）  =  300
                                   缺省动作  =  丢弃
                             缺省重定向名称  =  NULL
                                 配置域名称  =  NULL
(结果个数 = 1)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-CFTEMPLATE.md`
