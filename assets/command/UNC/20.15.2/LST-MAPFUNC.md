---
id: UNC@20.15.2@MMLCommand@LST MAPFUNC
type: MMLCommand
name: LST MAPFUNC（查询MAP功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MAPFUNC
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- MAP应用协议
- MAP功能配置
status: active
---

# LST MAPFUNC（查询MAP功能配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查看MAP功能配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [MAP功能配置（MAPFUNC）](configobject/UNC/20.15.2/MAPFUNC.md)

## 使用实例

查询MAP功能配置中所有相关的功能项:

LST MAPFUNC:;

```
%%LST MAPFUNC:;%%
RETCODE = 0  操作成功。

MAP 功能流程表
--------------
           分段插入鉴权集  =  支持
             GPRS增强功能  =  支持
                  MAP版本  =  版本2+
          是否支持SPS功能  =  不支持
                  缺省EIR  =  NULL
是否支持Reattach Required  =  支持
              PSI功能开关  =  不支持
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MAP功能配置(LST-MAPFUNC)_72225147.md`
