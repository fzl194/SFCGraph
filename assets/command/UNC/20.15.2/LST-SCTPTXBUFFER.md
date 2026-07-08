---
id: UNC@20.15.2@MMLCommand@LST SCTPTXBUFFER
type: MMLCommand
name: LST SCTPTXBUFFER（查询SCTP发送缓冲区参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCTPTXBUFFER
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

# LST SCTPTXBUFFER（查询SCTP发送缓冲区参数）

## 功能

**适用NF：SGSN、MME、AMF**

该命令用于查询系统中SCTP发送缓冲区参数。

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

- [SCTP发送缓冲区参数（SCTPTXBUFFER）](configobject/UNC/20.15.2/SCTPTXBUFFER.md)

## 使用实例

查询发送端缓冲区共享模式下的参数信息：

```
LST SCTPTXBUFFER: MODE=SHARE;
```

```
查询结果如下
-------------------------
                    模式选项  =  共享模式
        迷你端私有缓冲区大小  =  20000
        迷你端共享缓冲区大小  =  50000
        迷你端共享缓冲区个数  =  600
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCTP发送缓冲区参数(LST-SCTPTXBUFFER)_81448868.md`
