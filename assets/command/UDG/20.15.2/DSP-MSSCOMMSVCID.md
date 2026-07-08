---
id: UDG@20.15.2@MMLCommand@DSP MSSCOMMSVCID
type: MMLCommand
name: DSP MSSCOMMSVCID（查询指定服务号的服务类型信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSCOMMSVCID
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 通信管理统计查询
status: active
---

# DSP MSSCOMMSVCID（查询指定服务号的服务类型信息）

## 功能

该命令用于查询指定服务号的服务类型信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示服务类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| SERVICEID | 服务号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示服务号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MSSCOMMSVCID]] · 指定服务号的服务类型信息（MSSCOMMSVCID）

## 使用实例

查询指定服务号的服务类型信息：

```
DSP MSSCOMMSVCID:RUNAME = "VNODE_VNRS_VNFC_IPU_0064",SERVICETYPE = 9,SERVICEID = 0;
```

```

RETCODE = 0  操作成功。

结果如下
--------
  服务实例使能状态  =  FALSE
        运行实例号  =  0
        部署线程号  =  0
      报文通信队列  =  0 0 0 0 0 0 0 0
      消息通信队列  =  0 0 0 0 0 0 0 0
  报文功能块号错误  =  0
    报文实例号错误  =  0
报文功能块缓存为空  =  0
报文功能块路选错误  =  0
  报文实例缓存为空  =  0
  报文实例没有注册  =  0
  报文队列索引错误  =  0
  报文流程没有适配  =  0
  消息功能块号错误  =  0
    消息实例号错误  =  0
消息功能块数据为空  =  0
消息功能块数据错误  =  0
消息功能块路选错误  =  0
  消息实例数据为空  =  0
  消息实例数据错误  =  0
  消息实例没有注册  =  0
  消息队列索引错误  =  0
  消息流程没有适配  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSCOMMSVCID.md`
