---
id: UNC@20.15.2@MMLCommand@LST BGP
type: MMLCommand
name: LST BGP（查询BGP）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BGP
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 设置BGP
status: active
---

# LST BGP（查询BGP）

## 功能

该命令用于查询BGP参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BGP]] · BGP（BGP）

## 使用实例

查询BGP参数：LST BGP：

```
LST BGP:;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
                BGP自治域号  =  100
                 使能GR能力  =  TRUE
            RIB结束时间（s） =  600
                    使能BGP  =  使能
                    BGP版本  =  4
             自治域路径上限  =  NULL
                     联盟ID  =  230
                   使能联盟  =  FALSE
     使能检查第一个自治域号  =  TRUE
使能VPN路由器的ID为自动选择  =  FALSE
               使能全部路由  =  FALSE
         启用内存限制的前缀  =  FALSE
      使能GR能力重置BGP连接  =  FALSE
      中断BGP对等体协议会话  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-BGP.md`
