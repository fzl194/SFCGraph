---
id: UNC@20.15.2@MMLCommand@LST SYS
type: MMLCommand
name: LST SYS（查询系统参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SYS
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 系统参数管理
status: active
---

# LST SYS（查询系统参数）

## 功能

**适用网元：SGSN、MME**

该命令用于查看 UNC 系统参数信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [系统参数（SYS）](configobject/UNC/20.15.2/SYS.md)

## 使用实例

查询系统信息：

LST SYS:;

```
%%LST SYS:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
           系统描述  =  UNC
           系统标识  =  1
           系统名称  =  UNC_1
           系统位置  =  NO LOCATION
           服务描述  =  UNC
         移动国家码  =  460
           移动网号  =  00
           协议版本  =  R4
         核心网标识  =  0
           设备能力  =  255
   TMSI资源分配方式  =  增强TMSI分配方式   
       签约数据存储  =  合并存储  
            S11标识  =  INVALID
    NRI容量限制开关  =  开启
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询系统参数(LST-SYS)_26146348.md`
