---
id: UDG@20.15.2@MMLCommand@LST FILTERINFO
type: MMLCommand
name: LST FILTERINFO（查询流过滤器下的所有过滤器信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FILTERINFO
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
- 流过滤器管理
- 流过滤器信息显示
status: active
---

# LST FILTERINFO（查询流过滤器下的所有过滤器信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询流过滤器下绑定的所有过滤器信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FILTERINFO]] · 流过滤器下的所有过滤器信息（FILTERINFO）

## 使用实例

运营商需要查询名称为ff1的流过滤器下的所有过滤器信息：

```
LST FILTERINFO: FLOWFILTERNAME="ff1";
```

```

RETCODE = 0  操作成功

过滤器信息
----------
          流过滤器名称  =  ff1
            过滤器名字  =  f1
三四层IPv4协议输入类型  =  字符串类型
三四层IPv6协议输入类型  =  NULL
    三四层协议数字类型  =  0
        三四层协议类型  =  ANY
    手机IP地址配置模式  =  NULL
        IP地址版本类型  =  IPV4
            手机IP地址  =  0.0.0.0
    手机IP地址掩码类型  =  反掩码地址类型
    手机IP地址掩码长度  =  0
      手机IP地址反掩码  =  255.255.255.255
          手机IPv6地址  =  ::
  手机IPv6地址掩码类型  =  反掩码地址类型
  手机IPv6地址掩码长度  =  0
    手机IPv6地址反掩码  =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
        手机IP列表名称  =  NULL
  服务器IP地址配置模式  =  Host
          服务器IP地址  =  0.0.0.0
  服务器IP地址掩码类型  =  反掩码地址类型
  服务器IP地址掩码长度  =  0
    服务器IP地址反掩码  =  255.255.255.255
        服务器IPv6地址  =  ::
服务器IPv6地址掩码类型  =  反掩码地址类型
服务器IPv6地址掩码长度  =  0
  服务器IPv6地址反掩码  =  FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF
          Host配置名称  =  host1
		          域名  =  www.host1.com
      服务器IP列表名称  =  NULL
        手机起始端口号  =  0
        手机结束端口号  =  65535
      服务器起始端口号  =  0
      服务器结束端口号  =  65535
           Tos配置类型  =  NULL
           Tos分类类型  =  NULL
              服务类型  =  NULL
              生效标记  =  否
            配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FILTERINFO.md`
