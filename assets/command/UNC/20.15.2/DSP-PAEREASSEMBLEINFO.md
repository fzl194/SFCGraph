---
id: UNC@20.15.2@MMLCommand@DSP PAEREASSEMBLEINFO
type: MMLCommand
name: DSP PAEREASSEMBLEINFO（显示PAE分片重组统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEREASSEMBLEINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 报文
status: active
---

# DSP PAEREASSEMBLEINFO（显示PAE分片重组统计信息）

## 功能

该命令用来查看指定资源内Fabric口分片重组统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAEREASSEMBLEINFO]] · PAE分片重组统计信息（PAEREASSEMBLEINFO）

## 使用实例

显示微服务“aa”上Fabric口分片重组统计信息：

```
DSP PAEREASSEMBLEINFO:CELLTYPE="aa", CELLINSTANCE="aa";
```

```
RETCODE = 0  操作成功。

结果如下
--------
                微服务类型  =  aa
              微服务实例号  =  aa				
    需要重组的分片报文数量  =  0
  分片报文重组后的报文数量  =  0
        重组失败的报文数量  =  0
需要进行分片处理的报文数量  =  0
      分片处理后的报文数量  =  0
          分片失败报文数量  =  0
          系统重组节点总数  =  4096
      当前使用的重组节点数  =  0
系统最多缓存的分片报文数量  =  8192
    当前缓存的分片报文数量  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PAEREASSEMBLEINFO.md`
