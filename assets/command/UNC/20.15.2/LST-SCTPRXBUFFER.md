---
id: UNC@20.15.2@MMLCommand@LST SCTPRXBUFFER
type: MMLCommand
name: LST SCTPRXBUFFER（查询SCTP接收缓冲区参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCTPRXBUFFER
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# LST SCTPRXBUFFER（查询SCTP接收缓冲区参数）

## 功能

**适用NF：SGSN、MME、AMF**

该命令用于查询系统中SCTP接收端缓冲区参数。

## 注意事项

无。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MODE | 模式选项 | 可选必选说明：可选参数<br>参数含义：该参数用于区分共享模式、私有模式下的参数配置。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- SHARE（共享模式）<br>- PRIVATE（私有模式）<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCTPRXBUFFER]] · SCTP接收缓冲区参数（SCTPRXBUFFER）

## 使用实例

查询接收端缓冲区共享模式下的参数信息：

```
LST SCTPRXBUFFER: MODE=SHARE;
```

```
查询结果如下
-------------------------
                  模  式选项  =  共享模式
           大缓冲区min块数目  =  5556
           大缓冲区min块大小  =  8502
           大缓冲区med块数目  =  23455
           大缓冲区med块大小  =  3162
           大缓冲区max块数目  =  197011
           大缓冲区max块大小  =  9784
           小缓冲区max块数目  =  146549
           小缓冲区max块大小  =  4698
           小缓冲区med块数目  =  198629
           小缓冲区med块大小  =  4230
           小缓冲区min块数目  =  132923
           小缓冲区min块大小  =  9397 
 大缓冲区单偶联max块最大块数  =  583 
 大缓冲区单偶联med块最大块数  =  918 
 大缓冲区单偶联min块最大块数  =  647 
 小缓冲区单偶联max块最大块数  =  726 
 小缓冲区单偶联med块最大块数  =  224
 小缓冲区单偶联min块最大块数  =  996
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SCTPRXBUFFER.md`
