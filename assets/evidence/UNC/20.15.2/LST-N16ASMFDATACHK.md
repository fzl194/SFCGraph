# 查询N16aSMF数据核查功能（LST N16ASMFDATACHK）

- [命令功能](#ZH-CN_MMLREF_0000001977579556__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001977579556__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001977579556__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001977579556__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001977579556__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001977579556)

**适用NF：SMF**

该命令用于查询N16aSMF数据核查功能，如是否支持基于UserAgent的数据核查。

## [注意事项](#ZH-CN_MMLREF_0000001977579556)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001977579556)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001977579556)

无

## [使用实例](#ZH-CN_MMLREF_0000001977579556)

查询所有N16ASMFDATACHK记录：

```
%%LST N16ASMFDATACHK:;%%
RETCODE = 0  操作成功

结果如下
------------------------
USERAGENTCHK  =  ON
```

## [输出结果说明](#ZH-CN_MMLREF_0000001977579556)

| 输出项名称 | 输出项解释 |
| --- | --- |
| UserAgent检查开关 | 该参数用于表示N16aSMF基于user agent信息检查的功能开关。当该开关打开时，N16aSMF作为服务端收到来自I-SMF发送的消息，且当消息中的http head中携带user agent时，根据user agent携带的客户端网元的Instance ID进行检查，如果该Instance ID与本地上下文中保存I-SMF的不一致，则给左侧回复404，反之不做额外处理。当该开关关闭时，N16aSMF不对user agent中信息进行检查。 |
