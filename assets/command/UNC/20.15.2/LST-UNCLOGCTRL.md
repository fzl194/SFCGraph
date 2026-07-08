---
id: UNC@20.15.2@MMLCommand@LST UNCLOGCTRL
type: MMLCommand
name: LST UNCLOGCTRL（查询UNC日志控制记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UNCLOGCTRL
command_category: 查询类
applicable_nf:
- SMF
- AMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# LST UNCLOGCTRL（查询UNC日志控制记录）

## 功能

**适用NF：SMF、AMF、NRF、NSSF、SMSF、NCG**

该命令用于查询UNC日志的控制记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：记录索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UNCLOGCTRL]] · UNC日志控制记录（UNCLOGCTRL）

## 使用实例

如下命令用于查询记录

```
%%LST UNCLOGCTRL: INDEX=1;%%
RETCODE = 0  操作成功

结果如下
--------
                索引  =  1
              CS名称  =  NULL
        文件或路径名  =  NULL
            代码行号  =  0
              函数名  =  NULL
              关键字  =  NULL
      是否打印调用栈  =  否
          白名单模式  =  否
设置匹配的日志的级别  =  INVALID
                描述  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UNCLOGCTRL.md`
